terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.6.2"
    }
  }

  # determines how state is loaded/stored
  # default: local storage
  backend "s3" {
    bucket = "myapp-bucket"
    key = "myapp/stage.tfstate"
    region = "eu-central-1"
  }
}

provider "aws" {
  region = var.region
}

resource "aws_vpc" "myapp-vpc" {
  cidr_block = var.vpc_cidr_block
  tags       = {
    Name : "${var.env_prefix}-vpc"
  }
}


resource "aws_subnet" "myapp-subnet-1" {
  vpc_id            = aws_vpc.myapp-vpc.id
  availability_zone = var.avail_zone
  cidr_block        = var.subnet_cidr_block
  tags              = {
    Name : "${var.env_prefix}-subnet-1"
  }
}

resource "aws_route_table" "myapp-route-table" {
  vpc_id = aws_vpc.myapp-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.myapp-igw.id
  }
  tags = {
    Name : "${var.env_prefix}-rtb"
  }
}

resource "aws_internet_gateway" "myapp-igw" {
  vpc_id = aws_vpc.myapp-vpc.id
  tags   = {
    Name : "${var.env_prefix}-igw"
  }
}

resource "aws_route_table_association" "a-rtb-subnet" {
  subnet_id      = aws_subnet.myapp-subnet-1.id
  #  vpc_id = aws_vpc.myapp-vpc.id
  route_table_id = aws_route_table.myapp-route-table.id
}

resource "aws_security_group" "myapp-sg" {
  name   = "myapp-sg"
  vpc_id = aws_vpc.myapp-vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.my_ip, var.jenkins_ip]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
    prefix_list_ids = []
  }
  tags = {
    Name : "${var.env_prefix}-security-group"
  }
}

data "aws_ami" "latest-amazon-linux-image" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}
resource "aws_instance" "myapp-server" {
  # --- required Attributes ---
  # Amazon Machine Image (OS)
  ami           = data.aws_ami.latest-amazon-linux-image.id
  # Server size
  instance_type = var.instance_type

  # --- optional Attributes ---
  subnet_id              = aws_subnet.myapp-subnet-1.id
  vpc_security_group_ids = [aws_security_group.myapp-sg.id]
  availability_zone      = var.avail_zone

  # should be accessible from outside
  associate_public_ip_address = true

  # name of the key-pair file for ssh connection
  # the file should be downloaded und put into .ssh folder
  # "chown 400 filename.pem"
  # ssh -i ~/.ssh/filename.pem ec2-user@servers.public.ip.address
  key_name = "server-key-pair"

  # kind of entrypoint of server
  # executed once on **initial start up** (not every start up)
  # --- passing data to AWS ---
  user_data = file("entry-script.sh")
  tags      = {
    Name : "${var.env_prefix}-server"
  }
}

output "ec2_public_ip" {
  value = aws_instance.myapp-server.public_ip
}