import json

JENKINS_TOKEN=""
JENKINS_URL="https://jenkins-equator.cicd.mn1.ocp.ascendmoney-dev.internal/job/equator-cicd/job/equator-cicd-report-prepare-promote-to-staging/buildWithParameters"

def getReleaseList(list_to_release):
    release_list = []
    with open(list_to_release, 'r') as f:
        for line in f:
            app = line.split()
            release_list.append(app)
    return release_list

# curl -k -X POST -H "Authorization: Bearer ${JENKINS_TOKEN}" ${JENKINS_URL} --data app_name=report --data app_version=4.40.2-1440

def getShellCommand(release_list):
    command_list = []
    for app_name in release_list:
        app_name = str(app_name[0])
        # Opening JSON file
        f = open(f'./dependencyDocs/{app_name}.json')
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        app_release_name = data['release_name']
        app_release_version = data['release_version']
        command = f"curl -k -X POST -H \"Authorization: Bearer $JENKINS_TOKEN\" $JENKINS_URL --data app_name={app_release_name} --data app_version={app_release_version}"
        command_list.append(command)
        # Closing file
        f.close()
    return command_list

release_list=getReleaseList(list_to_release='./list_to_release')
shell_command_list = getShellCommand(release_list)
print(shell_command_list[0])
print(shell_command_list[1])


