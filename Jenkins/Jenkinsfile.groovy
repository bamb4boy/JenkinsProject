pipeline {
    agent any
    
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('check working directory')
            steps {
                sh "pwd"
            }
         }
     }
}  
