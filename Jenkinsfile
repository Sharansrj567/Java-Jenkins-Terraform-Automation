#!/usr/bin/env groovy

def gv

pipeline {
    agent any
    tools {
        maven 'maven-3.6'
    }
    stages {
       stage("init") {
           steps {
               script {
                   gv = load "script.groovy"
               }
           }
       }

        stage("increment version") {
            steps {
                script {
                    echo 'incrementing app version ...'
                   sh 'mvn build-helper:parse-version versions:set -DnewVersion=\\${parsedVersion.majorVersion}.\\${parsedVersion.minorVersion}.\\${parsedVersion.nextIncrementalVersion} versions:commit'
                   def matcher = readFile('pom.xml') =~ '<version>(.+)</version>'
                   def version = matcher[0][1]
                   env.IMAGE_NAME = "$version-$BUILD_NUMBER"
                }
            }
        }

        stage("build jar") {
            steps {
                script {
                    echo "building jar"
                   sh 'mvn clean package'
                   gv.buildJar()
                }
            }
        }
        stage("build image") {
            steps {
                script {
                    echo "building image"
                   withCredentials([usernamePassword(credentialsId: 'docker-hub-repo', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                       sh "docker build -t aavertsev/demo-app:${IMAGE_NAME} ."
                       sh "echo $PASS | docker login -u $USER --password-stdin"
                       sh "docker push aavertsev/demo-app:${IMAGE_NAME}"
                   }
                    gv.buildImage()
                }
            }
        }

        stage('provision server') {
            environment {
                AWS_ACCESS_KEY_ID = credentials('jenkins_aws_access_key_id')
                AWS_SECRET_ACCESS_KEY = credentials('jenkins_aws_secret_access_key')
                TF_VAR_env_prefix = 'test'
            }
            steps {
                script {
                    dir('terraform') {
                        sh "terraform init"
                        sh "terraform apply --auto-approve"
                        EC2_PUBLIC_IP = sh(
                            script: "terraform output ec2-public_ip"
                            returnStdout: true
                        ).trim()
                    }
                }
            }
        }

        stage("deploy") {
            environment {
                DOCKER_CREDS = credentials('docker-hub-repo') // creates automatically DOCKER_CREDS_USR and DOCKER_CREDS_PSW
            }
            steps {
                script {
                    echo "waiting for EC2 server to initialize"
                    sleep(time: 90, unit: "SECONDS")

                    echo "deploying docker image to EC2..."
                    echo "${EC2_PUBLIC_IP}"
                    IMAGE_NAME = 'aavertsev/demo-app:1.0'
                    def shellCmd = "bash ./server-cmds.sh ${IMAGE_NAME} ${DOCKER_CREDS_USR} ${DOCKER_CREDS_PSW}"
                    def ec2Instance = "ec2-user@${EC2_PUBLIC_IP}"

                    sshagent(['ec2-server-key']) {
                        sh "scp -o StrictHostKeyChecking=no docker-compose.yml ${ec2Instance}:/home/ec2-user"
                        sh "scp -o StrictHostKeyChecking=no server-cmds.sh ${ec2Instance}:/home/ec2-user"
                        sh "ssh -o StrictHostKeyChecking=no ${ec2Instance} ${shellCmd}"
                    }
                }
            }
        }
        stage('commit version update') {
            steps{
                script {
                    echo 'commit version update'
                    withCredentials([sshUserPrivateKey(credentialsId: 'github-ssh-key', keyFileVariable: 'SSH_KEY', passphraseVariable: '', usernameVariable: 'SSH_USER')]) {
                        sh "git remote set-url origin git@github.com/Sharansrj567/Java-Jenkins-Terraform-Automation.git"
                        sh 'git add .'
                        sh 'git commit -m "ci: version bump"'
                        sh 'GIT_SSH_COMMAND="ssh -i $SSH_KEY" git push origin HEAD:main'
                    }
                }
            }
        }
    }
}