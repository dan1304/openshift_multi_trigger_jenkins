#!/bin/bash
# replace with your namespace to get correct token
OCP_JENKINS_URL="https://jenkins-equator.cicd.mn1.ocp.ascendmoney-dev.internal/job/equator-cicd/job/equator-cicd-"
OCP_JENKINS_SECRET=$(oc get secret -n equator-cicd | grep jenkins-token  | awk 'NR==1{print $1; exit}')
OCP_JENKINS_TOKEN=$(oc get secret -n equator-cicd ${OCP_JENKINS_SECRET} -o=jsonpath={.data.token} | base64 -D)

echo "OCP_JENKINS_URL=\"${OCP_JENKINS_URL}"\" > ./.env
echo "OCP_JENKINS_TOKEN=\"${OCP_JENKINS_TOKEN}"\" >> ./.env
