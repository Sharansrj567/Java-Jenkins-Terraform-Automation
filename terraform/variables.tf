variable "region" {
  default = "eu-central-1"
}
variable "avail_zone" {
  default = "eu-central-1a"
}
variable "vpc_cidr_block" {
  default = "10.0.0.0/16"
}
variable "subnet_cidr_block" {
  default = "10.0.10.0/24"
}
variable "env_prefix" {
  default = "dev"
}
variable "my_ip" {
  default = "91.66.120.184/32"
}
variable "jenkins_ip" {
  default = "165.22.75.157/32"
}
variable "instance_type" {
  default = "t2.micro"
}
