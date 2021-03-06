pipeline {
    agent {
        label 'jnlp-slave'
    }

    environment {
        PROJECT_NAME="phoenix"
        APPLICATION_NAME="ansible-api"

        REPOSITORY_URL = "https://github.com/buxiaomo/ansible-api.git"

        REGISTRY_PROTOCOL="https"
        REGISTRY_URL = "hub.xiaomo.io"
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '15'))
    }

    stages {
        stage('checkout') {
            steps {
                git url: "${env.REPOSITORY_URL}"
            }
        }

        stage('build') {
            steps {
                container('dockerd') {
                    sh label: 'Docker Image', script: "docker build -t ${env.REGISTRY_URL}/${env.PROJECT_NAME}/${env.APPLICATION_NAME}:${BUILD_ID} ."
                }
            }
        }

        stage('push') {
            steps {
                container('dockerd') {
                    withDockerRegistry(credentialsId: "${env.REGISTRY_AUTH}", url: "${env.REGISTRY_PROTOCOL}://${env.REGISTRY_URL}") {
                        sh label: 'Docker', script: "docker push ${env.REGISTRY_URL}/${env.PROJECT_NAME}/${env.APPLICATION_NAME}:${BUILD_ID}"
                    }
                }
            }
        }

        stage('deploy dev') {
            steps {
                container('kubectl') {
                    sh label: 'namespace', script: "kubectl get ns ${env.PROJECT_NAME}-dev || kubectl create ns ${env.PROJECT_NAME}-dev"
                    sh label: 'change tag', script: "sed -i \"s#IMAGE_TAG#${BUILD_ID}#\" ./manifests/deployment.yaml"
                    sh label: 'deploy', script: "kubectl apply -n ${env.PROJECT_NAME}-dev -f ./manifests/deployment.yaml"
                }
            }
        }
    }
}