#!/bin/bash

read -p "Enter Application Name:" appName

echo "********************************************************"
echo "  Launching Helm Chart "
echo "********************************************************"

helm install ${appName} $PWD/helm/hello-world/


echo "*********************************************************"
echo "  Please be patient while the chart is being deployed"
echo "*********************************************************"

sleep 30

echo "**********************************************************"
echo "  ${appName}  Launched "
echo "**********************************************************"


echo "**********************************************************"
echo "  Use Following URL To Launch The App On Browser "
echo "**********************************************************"

minikube service ${appName}-wordpress



