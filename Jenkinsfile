pipeline {
    agent { docker { image 'sample-image' } }
    stages {
        stage('Test') {
            steps {
                sh 'python3.8 -m unittest'
            }
        }
    }
}
