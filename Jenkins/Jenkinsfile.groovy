def userInput

pipeline {

    agent {
        label 'docker_node'
    }

    stages {
        stage('Build Docker image') {
            steps {
                dir('coronadata'){
                    script {
                        sh "sudo docker build -t coronadata ."
                    }
                }
            }
        }
        stage('Test Docker image') {
            steps {
                dir('coronadata/tests') {
                    script{
                        try {
                            sh "sudo /home/gleb/JenkinsProject/coronadata/tests/basic.test.sh"
                        } catch (err) {
                            println("Error thrown on test file execution")
                            currentBuild.result = 'ABORTED'
                            error('Error thrown on test file execution')
                        }
                    }
                }
            }
        }
        stage('Upload image to repository') {
            steps {
                sh "pwd"
            }
        } 
        
    }
}
