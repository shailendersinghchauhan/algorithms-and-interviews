#!groovy
/*
File: Jenkinsfile
Project: MFH
Purpose: Configured under Jenkins and deploys most of valid  build
Author: Shailender Singh
Version:
--------------------------------------------------------------------------
S.no | Version | Update By | Date                   | Comments
--------------------------------------------------------------------------
 1.  | 0.1     | Shailender| May 19 2022            |Pushed to develop branch (final script)

*/

pipeline {
  agent { label 'Windows' } # agent all

  parameters {
    choice(name: 'Module', choices: 'app1\napp2\nall', description: 'application module?')
    choice(name: 'Environment', choices:'develop\ndevelop2\ndevelop3\nqa\nqa2\nqa3', description: 'deployment environment?')
  }

  environment {
    SLACK_CHANNEL = '#mfh'
    GIT_CREDS_ID = 'github-creds'

  }

  stages {
    stage('Setup') {
      steps {
            dir ("build-scripts") {
              git url: 'https://github.com/shailendersinghchauhan/algorithms-and-interviews', branch: 'develop', credentialsId: "${env.GIT_CREDS_ID}"
			  sh 'pwd;echo $PWD'
			  sh './build-packer-image.ps1'
            }

          }
        }
      }
    }

  post {
    success {
      // Only clean workspace on success. Leave failed builds for postmortem review
      cleanWs()
      slackSend(channel: "${env.SLACK_CHANNEL}", color: "good",
        message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} Success after ${currentBuild.durationString.replace('and counting', '')} ${params.Module}  (<${env.BUILD_URL}|Open>)")
    }
    aborted {
      slackSend(channel: "${env.SLACK_CHANNEL}", color: "warning",
        message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} ABORTED after ${currentBuild.durationString.replace('and counting', '')} (<${env.BUILD_URL}|Open>) @here")
    }
    failure {
      slackSend(channel: "${env.SLACK_CHANNEL}", color: "danger",
        message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} FAILURE after ${currentBuild.durationString.replace('and counting', '')} (<${env.BUILD_URL}|Open>)")
    }
  }
}