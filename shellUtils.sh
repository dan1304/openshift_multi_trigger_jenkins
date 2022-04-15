# replace with your namespace to get correct token
OCP_JENKINS_SECRET=$(oc get secret -n #Your_Namespace# | grep jenkins-token  | awk 'NR==1{print $1; exit}')
OCP_JENKINS_TOKEN=$(oc get secret -n #Your_Namespace# ${OCP_JENKINS_SECRET} -o=jsonpath={.data.token} | base64 -D)
