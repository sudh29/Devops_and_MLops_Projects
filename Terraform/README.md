uv init

uv venv

source .venv/bin/activate

terraform plan

terraform plan -var 'user=["Ram","Shyam"]'

terraform plan -var-file=dev.tfvars

export TF_VAR_username=user1

terraform fmt
terraform init
terraform providers
terraform validate
terraform plan
terraform apply
terraform apply --auto-approve
terraform destroy
terraform destroy --target github_repository.terraform_myrepo
terraform refresh
terraform show
terraform output
terraform console
exit

ssh-keygen -t rsa -b 4096 -C "aws_tf_key"

ssh -i ubuntu@172.31.6.64
