pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building stage!'
                sh 'make build'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make test-unit'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('Unit test API') {
            steps {
                sh 'make test-api'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('Unit test E2E') {
            steps {
                sh 'make test-e2e'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
    }
    post {
        always {
            junit 'results/*_result.xml'
            cleanWs()
        }
        success {  
             echo 'This will run only if successful'  
             mail to: 'bpgtoapanta@gmail.com', body: "<b>Pipeline - ERROR Compile</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", charset: 'UTF-8', mimeType: 'text/html', subject: "ERROR CI: Project name -> ${env.JOB_NAME}";  
         }  
         failure {  
             mail to: 'bpgtoapanta@gmail.com', body: "<b>Pipeline - ERROR Compile</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", charset: 'UTF-8', mimeType: 'text/html', subject: "ERROR CI: Project name -> ${env.JOB_NAME}";  
         }  
    }
}
