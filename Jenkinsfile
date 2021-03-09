pipeline {
    agent { docker { image 'sample-image' } }
    stages {
        stage('Test') {
            steps {
                sh 'python -m unittest'
            }
        }
    }
}
