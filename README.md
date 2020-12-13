# Simple-Web-App

   Web application connects to a database on kubernetes cluster, reads and returns those data's upon HTTP request.
     
   
   # Prerequisites 
      
     - Git 
     - Docker 1.13.1
     - Helm 3.4.2
     - MiniKube 1.15.1
     - Kubectl 1.19
     - PV provisioner support in the underlying infrastructure
     
   # Steps To Run The Application
   
       - git clone https://github.com/hussaintr/simple-web-app.git
       - cd simple-web-app
       - chmod +x run.sh
       - Execute ./run.sh 
           - Enter Application Name:  <Hello>
               *Replace <> with requied App Name
               
   #  To Check Running Pod
         kubectl get pods
    
   #  To Check Running Services
         kubectl get svc
         
   #  To Check Persistent Volumes
         kubectl get pv
   
   #  To Uninstall Application
         helm uninstall <App Name>
         
   #  Helm Uninstall Should Delete Resources PVC & PV. If not, do it manually
         kubectl get pvc
         # If Status is in 'Bound' state, then delete it manually 
         kubectl delete pvc <Name>
         
