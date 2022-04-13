import subprocess
# curl -k -X POST -H "Authorization: Bearer $JENKINS_TOKEN" $JENKINS_URL --data app_name=voucher --data app_version=4.40.4-48
# //pipe = subprocess.Popen(['curl', '-k' , URL], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
# $(oc get secret jenkins-token-7ftpf -o=jsonpath={.data.token} | base64 -D)\n

class ocUtils:
    def __init__(self, env):
        self.env = env

    def getJenkinsToken(self):
        self.jenkinsToken = subprocess.run(['oc', 'get', 'secret', 'jenkins-token-7ftpf', '-o=jsonpath={.data.token}', '| base64 -D'], stdout=subprocess.PIPE).stdout
        return self.jenkinsToken
