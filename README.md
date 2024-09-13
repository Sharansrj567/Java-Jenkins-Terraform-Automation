
# Java Jenkins Terraform Project

This project demonstrates a comprehensive deployment of a Java application using Jenkins for CI/CD, Docker for containerization, and Terraform for infrastructure as code (IaC) on AWS. The Java application, `CodeSanitize`, is a security-focused application developed in Spring Boot, which aims to detect vulnerabilities and prevent data poisoning in large language models (LLMs).

## Project Structure

- **`.gitignore`**: Specifies files and directories to ignore in version control.
- **`docker-compose.yml`**: Defines multi-container Docker applications.
- **`Dockerfile`**: Specifies the environment and application configuration for Docker.
- **`Jenkinsfile`**: Contains the pipeline script for Jenkins to automate build, test, and deployment.
- **`pom.xml`**: Maven configuration file to manage dependencies and build the project.
- **`script.groovy`**: Groovy script for Jenkins pipeline tasks.
- **`server-cmds.sh`**: Shell script containing server-related commands.
- **`src/`**: Contains the source code for the application.
  - **`main/`**: Main source directory.
    - **`java/`**: Contains Java source files.
      - **`com/sharansrj567/CodeSanitizeApplication.java`**: Entry point of the Spring Boot application. This file initializes the `CodeSanitize` application, which provides APIs for detecting vulnerabilities in AI models and preventing data poisoning.
    - **`resources/`**: Contains application resources.
      - **`templates/index.html`**: Static HTML file for the application, which provides a user interface for interacting with the `CodeSanitize` application.
      - **`application.properties`**: Configuration file for the Spring Boot application.
- **`terraform/`**: Contains Terraform configuration files for infrastructure management.
  - **`entry-script.sh`**: Startup script executed on the EC2 instance.
  - **`main.tf`**: Main Terraform configuration file.
  - **`variables.tf`**: Variables used in Terraform configuration.

## Prerequisites

Ensure the following prerequisites are installed and configured:

- Java 8
- Maven
- Docker
- Jenkins
- Terraform
- AWS CLI

## Application Overview

The `CodeSanitize` application is a Spring Boot application designed to detect and prevent vulnerabilities and data poisoning attacks in large language models (LLMs). It was initially implemented in Python using Flask APIs but has been migrated to Java Spring Boot to leverage enterprise-level scalability and enhanced security features.

### Running the Application Locally

To run the application locally:

```sh
mvn spring-boot:run
```

## Docker

The Docker configuration is defined in the `Dockerfile`, which allows containerization of the `CodeSanitize` application.

### Building the Docker Image

To build the Docker image:

```sh
docker build -t code-sanitize-app .
```

### Running the Docker Container

To run the Docker container:

```sh
docker run -p 8080:8080 code-sanitize-app
```

## Docker Compose

The Docker Compose configuration is defined in `docker-compose.yml`.

### Running with Docker Compose

To start the services using Docker Compose:

```sh
docker-compose up
```

## Jenkins

The Jenkins pipeline is defined in the `Jenkinsfile` and `script.groovy`.

### Jenkins Pipeline Steps

- **Build Jar**: Compiles the application and packages it into a JAR file.
- **Build Image**: Builds the Docker image and pushes it to Docker Hub.
- **Deploy App**: Deploys the application using Docker or a cloud platform.

## Terraform

The Terraform configuration is located in the `terraform` directory.

### Variables

The variables are defined in `variables.tf`.

### Main Configuration

The main configuration is defined in `main.tf`.

### Applying the Terraform Configuration

To apply the Terraform configuration:

```sh
cd terraform
terraform init
terraform apply
```

## Scripts

### Server Commands

The server commands are defined in `server-cmds.sh`.

### Entry Script

The entry script for the EC2 instance is defined in `entry-script.sh`.

## Resources

- **`index.html`**: The static HTML file for the application provides a UI for interacting with the application’s features.

## License

This project is licensed under the MIT License.

Feel free to modify the content as per your specific requirements.
