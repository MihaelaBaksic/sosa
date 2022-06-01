pipeline{
	agent any
	stages {
		stage('Clone'){
			steps{
				echo 'Cloning...'
				sh 'pwd'
				sh 'ls $PWD'
			}
		}
		stage('Test'){
			steps{
				echo 'Testing'
			}
		}
		stage('Deploy'){
			steps{
				echo 'Deploying'
			}
		}
	}
	
}
