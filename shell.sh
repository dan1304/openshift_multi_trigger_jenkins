
export JENKINS_URL="https://jenkins-equator.cicd.mn1.ocp.ascendmoney-dev.internal/job/equator-cicd/job/equator-cicd-report-prepare-promote-to-staging/buildWithParameters"
export JENKINS_TOKEN=$(oc get secret jenkins-token-7ftpf -o=jsonpath={.data.token} -n equator-cicd | base64 -D)


export JENKINS_URL="https://jenkins-equator.cicd.mn1.ocp.ascendmoney-dev.internal/job/equator-cicd/job/equator-cicd-report-prepare-promote-to-staging/buildWithParameters"

curl -k -X POST -H "Authorization: Bearer ${JENKINS_TOKEN}" ${JENKINS_URL} --data app_name=report --data app_version=4.40.2-1440
