pipeline{
	agent any
	environment {
        TIMESTAMP = '$(date +"%d-%m-%Y_%H:%M:%S")'
    }
	stages {
		stage('Prep'){
			steps{
				sh 'ls $PWD'
				sh 'echo $TIMESTAMP'
				sh 'mkdir logs-$TIMESTAMP'
			}
		}
		stage('Test'){
			steps{
				sh 'echo $TIMESTAMP'
				sh 'python test.py 2>&1 | tee /logs-$TIMESTAMP/ls.txt'
			}
		}
		stage('Predeploy'){
			steps{
				sh 'echo $TIMESTAMP'
			}
		}
		stage('Deploy'){
			steps{
				echo 'Deploying'
			}
		}
	}
	
}
