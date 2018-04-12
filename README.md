# monitor-rabbitmq
AWS Cloudwatch for rabbitmq

## Setup Environment variables
```bash
RABBIT_MQ_URL = 'http://localhost:15672' # default
RABBIT_MQ_USERNAME = 'guest' #default
RABBIT_MQ_PASSWORD = 'guest' # default
```

## Setup AWS Credentials
Also setup the AWS credentials `~/.aws/credentials` that have access to cloudwatch metrics.

## Setup the repo
```bash
pip3 install -r requirements.txt
```

## Setup a cron
Setup a cron that executes the python script as often as you want

Example:

Send metric every minutes
```bash
* * * * * python3 /home/ubuntu/monitor-rabbitmq/app.py
```

