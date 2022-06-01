pipeline{
	agent any
	environment {
        def TIMESTAMP = sh(script: 'echo $(date +"%d-%m-%Y_%H:%M:%S")', returnStdout: true).trim()
    }
	stages {
		stage('Prep'){
			steps{
				sh 'echo $TIMESTAMP'
				sh 'echo $TAG_UNIXTIME'
				sh 'echo $TAG_TIMESTAMP'
			}
		}
		stage('Test'){
			steps{
				sh 'echo $TIMESTAMP'
				sh 'python test.py 2>&1 | tee ./logs-$TIMESTAMP/ls.txt'
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
