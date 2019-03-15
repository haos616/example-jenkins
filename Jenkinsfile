#!/usr/bin/env groovy

pipeline {
  agent {
    node {
      label 'master'
    }
  }

  stages {
    stage('Stage name') {
      steps {
        sh 'echo build'
      }
    }

    stage('Parallel test') {
      parallel {
        stage('Parallel test 1') {
          steps {
            sh 'echo Parallel1'
          }
        }
        stage('Parallel test 2') {
          steps {
            sh 'echo Parallel2'
          }
        }
      }
    }

    stage('Stage name 2') {
      steps {
        sh 'echo Hello'
        sh 'whoami'
        sh 'ls -la'
      }
    }
  }

  post {
    always {
      sh 'echo always'
    }
    success {
      sh 'echo success'
    }
    failure {
      sh 'echo failure'
    }
    aborted {
      sh 'echo aborted'
    }

  }

}
