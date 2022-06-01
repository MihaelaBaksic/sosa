pipeline{
	agent any
	environment {
        TIMESTAMP = sh 'echo $(date +"%d-%m-%Y_%H:%M:%S")'
    }
	stages {
		stage('Prep'){
			steps{
				sh 'ls $PWD'
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
