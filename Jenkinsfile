pipeline {
    agent any

    environment {
        ACR_NAME        = 'your-acr-name'
        ACR_REGISTRY    = "${ACR_NAME}.azurecr.io"
        IMAGE_NAME      = 'git-test-app'
        IMAGE_TAG       = "${BUILD_NUMBER}"
        MANIFEST_REPO   = 'https://gitlab.com/your-group/manifest-repo.git'
        MANIFEST_BRANCH = 'main'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${ACR_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Push to ACR') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'acr-credentials',
                    usernameVariable: 'ACR_USER',
                    passwordVariable: 'ACR_PASS'
                )]) {
                    sh "docker login ${ACR_REGISTRY} -u ${ACR_USER} -p ${ACR_PASS}"
                    sh "docker push ${ACR_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }

        stage('Update Manifest Repo') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'gitlab-credentials',
                    usernameVariable: 'GIT_USER',
                    passwordVariable: 'GIT_PASS'
                )]) {
                    sh """
                        git clone https://${GIT_USER}:${GIT_PASS}@${MANIFEST_REPO.replace('https://', '')} manifest
                        cd manifest
                        sed -i 's|image: .*|image: ${ACR_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}|' deployment.yaml
                        git config user.email 'jenkins@ci.com'
                        git config user.name 'Jenkins'
                        git add deployment.yaml
                        git commit -m 'Update image tag to ${IMAGE_TAG}'
                        git push origin ${MANIFEST_BRANCH}
                    """
                }
            }
        }
    }

    post {
        always {
            sh "docker rmi ${ACR_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} || true"
        }
    }
}
