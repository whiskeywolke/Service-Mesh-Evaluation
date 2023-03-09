# Service Mesh Evaluation

## This Repository holds the content of the work I have done for the P1 Project "Service Meshes like Istio"

In this project I evaluated the impact of service meshes on the overall performance by utilizing Prometheus and Grafana on Kubernetes Clusters. 
To achieve this I have tested multiple microservice applications and visualized the results with custom Grafana dashboards.

You can find the report here [Report.pdf](Report.pdf).


## Description of folders & Files
- bookinfo :
	This folder holds all deployment files for the bookinfo microservice application as well as the corresponding analysis I have done using this application.
	It also contains the custom loadgenerator I developed as well as the resulting benchmark files
- dashboards :
	This folder contains the versions of the grafana dashboards I used to visualize key performance indicators of the deployed microservice application
- google-example-kubernetes-istio :
	This folder contains various files neccessary for deployment of this reference application
- old :
	this folder holds various files which do not contribute to the final outcome but provided interesting insights on which I based my decisions
- teastore :
	this folder holds the neccessary files for deployment of the teastore reference application as well as the custom load generator
- project_overview.md :
	A brief summary of the work I have done and how I approached different interesting topics during the semester
- Report.pdf :
	A detailed Report giving background information as well explanation of measurement results as well as a future outlook	
