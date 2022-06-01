pipeline{
	agent any
	stages {
		stage('Clone'){
			steps{
				sh 'ls $PWD'
			}
		}
		stage('Test'){
			steps{
				sh 'python test.py'
			}
		}
		stage('Deploy'){
			steps{
				echo 'Deploying'
			}
		}
	}
	
}
