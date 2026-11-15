# Deploying a Python Application on Kubernetes Using Minikube

## 1. Setting up the cluster

I began by installing Docker Desktop and Minikube through Homebrew, which also installed kubectl. Once Docker’s engine was running, I entered `minikube start --driver=docker` to create the cluster on my Mac. The first startup downloaded the Kubernetes components before configuring the environment. I checked the result with `kubectl get nodes`; the node showed “Ready”, confirming that I could proceed with deployment.

## 2. Preparing the application

I created a small Python application that returns a message when accessed through a browser. I kept its functionality simple so I could focus on how the application was packaged and managed. Its message and port are read from environment variables rather than fixed in the source code. This follows Wiggins’ (2017) guidance on separating configuration from code. The application does not store sessions or write persistent data, so neither instance depends on information held by the other.

## 3. Building the Docker image

Next, I created a Dockerfile using `python:3.13-slim`. It copies the application into the container and starts it using Python. No external Python packages were needed because the application uses the standard library. I configured it to run as a non-root user and enabled unbuffered output for logging.

I built the image with `docker build -t unit5-app:v1 .`, then loaded it into Minikube using `minikube image load unit5-app:v1`. This made the image available locally without uploading it to a public registry.

## 4. Configuring the deployment

I defined three resources in `deployment.yaml`: a ConfigMap, a Deployment and a Service. The ConfigMap holds the message and port settings. The Deployment specifies two replicas of the application, while the Service provides a consistent way to address them.

I included CPU and memory requests and limits, plus a readiness probe that checks the HTTP endpoint. A running container is not necessarily ready to answer requests, so this check provides a more useful indication of availability. The two replicas demonstrate the process-based approach to scaling described by Wiggins (2017), although I did not conduct a load test.

## 5. Checking the result

I applied the file with `kubectl apply -f deployment.yaml` and checked the rollout. Both pods reached “Running” status and showed `1/1` readiness. The Deployment therefore reached its declared replica count (Kubernetes Authors, n.d.).

To access the application, I ran `kubectl port-forward service/unit5-app 8080:80` and opened `http://localhost:8080`. My configured message appeared in the browser. I then checked the logs using `kubectl logs -l app=unit5-app --tail=5`, which showed HTTP 200 responses from both pods.

## 6. What the exercise demonstrated

This deployment helped me distinguish packaging an application from managing its execution. Docker supplied the image; Kubernetes managed its replicas and configuration. However, both pods share one node, so this setup cannot withstand node failure. It demonstrates several Twelve-Factor principles rather than complete compliance. Graceful shutdown handling and production access would need further work. The browser and log checks confirmed basic operation, but they did not establish performance, resilience under failure or production readiness.

## References

Kubernetes Authors (n.d.) *Using kubectl to create a Deployment*. Available at: https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/ (Accessed: 15 November 2026).

Wiggins, A. (2017) *The Twelve-Factor App*. Available at: https://12factor.net/ (Accessed: 15 November 2026).
