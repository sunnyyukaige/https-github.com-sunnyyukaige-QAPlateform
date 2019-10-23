pipeline{
    agent any
    stages {
    

    stage('Checkout') {
        steps{
            checkout scm
        }
    }
  
    stage('Publish') {
      steps{
        sh 'docker-compose build'
        echo 'docker-compose build finished'
        sh 'docker-compose up'
        echo 'docker-compose up finished' 
        }
    }
}

}