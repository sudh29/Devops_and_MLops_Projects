uv init

uv venv

source .venv/bin/activate

terraform plan

terraform plan -var 'user=["Ram","Shyam"]'

terraform plan -var-file=dev.tfvars

export TF_VAR_username=user1
