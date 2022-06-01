pipeline{
	agent any
	stages {
		stage('Clone'){
			steps{
				echo 'Cloning...'
				sh 'git clone https://github.com/MihaelaBaksic/sosa /home/mihaela/Documents/fer/2_semestar/SOSA/lab3/test'
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
