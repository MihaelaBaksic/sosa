pipeline{
	agent any
	environment {
        def TIMESTAMP = sh(script: 'echo $(date +"%d-%m-%Y_%H:%M:%S")', returnStdout: true).trim()
    }
	stages {
		stage('Prep'){
			steps{
				sh 'mkdir logs-$TIMESTAMP'
			}
		}
		stage('Test'){
			steps{
				sh 'echo $TIMESTAMP'
				sh 'python test.py 2>&1 | tee ./logs-$TIMESTAMP/unittest > /dev/fd/2'
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
