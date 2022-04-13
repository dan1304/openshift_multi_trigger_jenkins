import subprocess
import json
from dotenv import load_dotenv
import os

load_dotenv(".env")
JENKINS_URL = os.getenv('JENKINS_URL')
JENKINS_TOKEN = os.getenv('JENKINS_TOKEN')

class releaseDetails:
    def __init__(self, app_name):
        self.app_name = app_name

    def getReleaseDetails(self):
        with open(f"./dependencyDocs/{self.app_name}.json", 'r') as f:
            data = json.load(f)
            app_release_name = data['release_name']
            app_release_version = data['release_version']
        return (app_release_name, app_release_version)

class jenkinsApiTrigger:
    def __init__(self, app_name, app_version, release_environment):
        self.app_name = app_name
        self.app_version =  app_version
        self.release_environment = release_environment
    
    def preparePromote(self):
        self.command = f"curl -k -X POST -H \"Authorization: Bearer {JENKINS_TOKEN}\" {JENKINS_URL}{self.app_name}-prepare-promote-to-{self.release_environment}/buildWithParameters --data app_name={self.app_name} --data app_version={self.app_version}"
        subprocess.check_output(self.command, shell=True, stderr=subprocess.STDOUT)
        message = f"[TRIGGERED][{self.app_name} {self.app_version}]: {JENKINS_URL}{self.app_name}-prepare-promote-to-{self.release_environment}"
        return message

    def promote(self):
        self.command = f"curl -k -X POST -H \"Authorization: Bearer {JENKINS_TOKEN}\" {JENKINS_URL}{self.app_name}-promote-to-{self.release_environment}/buildWithParameters  --data app_name={self.app_name} --data app_version={self.app_version}"
        subprocess.check_output(self.command, shell=True, stderr=subprocess.STDOUT)
        message = f"[TRIGGERED][{self.app_name} {self.app_version}]: {JENKINS_URL}{self.app_name}-promote-to-{self.release_environment}"
        return message

    def checkPipelineStatus(self):
        pass

