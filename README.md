# monitor-rabbitmq
AWS Cloudwatch for rabbitmq

RabbitMQ monitoring with cloudwatch namespace as `Resource/RabbitMQ`. Each metric has the name that of the queue with count that of their existing message count. A special metric named `TotalMessages` that measures total number of messages in all queues. 

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

