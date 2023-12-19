import pulumi
from pulumi_gcp import container, serviceaccount, projects
from pulumi_kubernetes import Provider
from pulumi import Output

# Create a GCP project
project = projects.Project("project")

# Enable Kubernetes API for the project
pulumi.gcp.projects.Service("service",
    service_id="container.googleapis.com",
    disable_on_destroy=False)

# Create a Service Account
account = serviceaccount.Account("account", 
    project=project.project_id,
    account_id="my-service-account",
    display_name="My Service Account")

# Assign roles to the Service Account
iam_policy = serviceaccount.IAMBinding("iam-policy",
    project=project.project_id,
    role="roles/container.admin",
    members=[pulumi.Output.apply(account.email, lambda email: f"serviceAccount:{email}")])

# Create the GKE cluster
cluster = container.Cluster("cluster",
    initial_node_count=2,
    node_version="v1.20.4-gke.2000",
    node_config=container.ClusterNodeConfigArgs(machine_type="n1-standard-1"),
    depends_on=[iam_policy],
)

# Create a Kubernetes provider instance that uses our GKE cluster from above
k8s_provider = Provider("k8s-provider", 
    kubeconfig=cluster.kubeconfig)

pulumi.export("kubeconfig", cluster.kubeconfig)