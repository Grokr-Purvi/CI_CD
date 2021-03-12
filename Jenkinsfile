pipeline {
    agent { docker { image 'sample-image' } }
    stages {
        stage('Test') {
            steps {
                sh 'python3.8 -m unittest'
            }
        }
        stage('Deploy'){
            steps {
                
                sh 'zip -r lambdacode.zip src/*'
                sh 'aws lambda update-function-code --function-name  lambdapurvi --zip-file fileb://lambdacode.zip'
                sh 'rm -rf lambdacode.zip'
                
                //sh 'aws cloudformation create-stack --stack-name stackforcicdambuj5555 --template-body file://formation.json --capabilities CAPABILITY_NAMED_IAM'
            }
        }
    }
}
