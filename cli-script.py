import boto3
import os
import subprocess
import argparse
import types

dev_accounts = [ "dev", "deveu"]

all_accounts = dev_accounts

account_info={
  "ww": {"id": , "region": "us-east-1"}
}

sts = boto3.client('sts')

def run_cli_cmd(account_name, cmd):
    response = sts.assume_role(
        RoleArn = 'arn:aws:iam::{}:role/CrossAccount'.format(account_info[account_name]["id"]),
        RoleSessionName = "CrossAccountUtil")

    os.environ['AWS_ACCESS_KEY_ID'] = response['Credentials']['AccessKeyId']
    os.environ['AWS_SECRET_ACCESS_KEY'] = response['Credentials']['SecretAccessKey']
    os.environ['AWS_SESSION_TOKEN'] = response['Credentials']['SessionToken']
    os.environ['AWS_DEFAULT_REGION'] = account_info[account_name]["region"]

    if isinstance(cmd, types.StringTypes):
        subprocess.call(cmd.split(), env=os.environ)
    else:
        subprocess.call(cmd, env=os.environ)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Run a cross-account aws cli command')
    parser.add_argument('-a', dest='account', help='The AWS account to use.')
    parser.add_argument('-c', dest='cmd', help='The command to run.')

    args = parser.parse_args()

    run_cli_cmd(args.account, args.cmd)
