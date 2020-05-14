import cliscript
import subprocess
import fileinput
import sys

#cliscript.run_cli_cmd("ww","aws ec2 describe-vpcs")
#cliscript.run_cli_cmd("ww","eksctl create cluster -f infra-setup/create-cluster.yaml")
#cliscript.run_cli_cmd("ww","kubectl apply -f secrets/secret.yaml")
#cliscript.run_cli_cmd("ww","kubectl apply -k 'github.com/kubernetes-sigs/aws-efs-csi-driver/deploy/kubernetes/overlays/stable/?ref=master'")
#proc = subprocess.Popen(cliscript.run_cli_cmd("ww","aws ec2 create-security-group --group-name eks-efs-sg --description connect-to-efs --output text"), shell=True, stdout=subprocess.PIPE, )
#SG_ID = proc.communicate()[0]
#print(SG_ID)
#VPC_ID = cliscript.run_cli_cmd("ww","aws eks describe-cluster --name react-app --query cluster.resourcesVpcConfig.vpcId --output text")
#SG_ID = cliscript.run_cli_cmd("ww","aws ec2 create-security-group --group-name eks-efs-sg --description connect-to-efs --output text")
