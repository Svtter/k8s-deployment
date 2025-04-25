helm repo add rancher-latest https://releases.rancher.com/server-charts/latest
helm repo update

kubectl create namespace cattle-system

kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.1/cert-manager.yaml

helm install rancher rancher-latest/rancher \
  --namespace cattle-system \
  --set hostname=rancher.yourdomain.com \
  --set replicas=1 \
  --set bootstrapPassword=admin

kubectl -n cattle-system port-forward svc/rancher 8443:443

# NOTE: Rancher may take several minutes to fully initialize. Please standby while Certificates are being issued, Containers are started and the Ingress rule comes up.
# Check out our docs at https://rancher.com/docs/
# If you provided your own bootstrap password during installation, browse to https://rancher.yourdomain.com to get started.

# If this is the first time you installed Rancher, get started by running this command and clicking the URL it generates:
# ```
# echo https://rancher.yourdomain.com/dashboard/?setup=$(kubectl get secret --namespace cattle-system bootstrap-secret -o go-template='{{.data.bootstrapPassword|base64decode}}')
# ```
# To get just the bootstrap password on its own, run:
# ```
# kubectl get secret --namespace cattle-system bootstrap-secret -o go-template='{{.data.bootstrapPassword|base64decode}}{{ "\n" }}'
# ```