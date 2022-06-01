pipeline{
	agent any
	stages {
		stage('Prep'){
			steps{
				sh 'ls $PWD'
				sh 'mkdir logs-$(date +"%d-%m-%Y-%H:%M:%S")'
			}
		}
		stage('Test'){
			steps{
				sh 'python test.py 2>&1 | tee /logs/ls.txt'
			}
		}
		stage('Predeploy'){
			steps{

			}
		}
		stage('Deploy'){
			steps{
				echo 'Deploying'
			}
		}
	}
	
}
