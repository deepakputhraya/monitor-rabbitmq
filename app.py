import requests
from requests.compat import urljoin
from requests.auth import HTTPBasicAuth
import boto3
import os
from utils.logging import logger as log

client = boto3.client('cloudwatch')

if 'RABBIT_MQ_URL' not in os.environ:
    URL = 'http://localhost:15672'
    log.info("Using default Admin URL %s", URL)
else:
    URL = os.environ['RABBITMQ_URL']

if 'RABBIT_MQ_USERNAME' not in os.environ:
    USERNAME = 'guest'
    log.info("Using default USERNAME %s", USERNAME)
else:
    USERNAME = os.environ['RABBITMQ_USERNAME']

if 'RABBIT_MQ_PASSWORD' not in os.environ:
    PASSWORD = 'guest'
    log.info("Using default PASSWORD")
else:
    PASSWORD = os.environ['PASSWORD']

requestURL = urljoin(URL, '/api/queues')


def put_metric(metrics):
    client.put_metric_data(
        Namespace='Resource/RabbitMQ',
        MetricData=metrics
    )


if __name__ == '__main__':
    total_messages = 0
    resp = requests.get(requestURL, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if resp.status_code == 200:
        queues = resp.json()
        count = 0
        metrics = []
        for q in queues:
            messages = q['messages']
            name = q['name']
            count = count + 1
            if count % 10 == 0:
                put_metric(metrics)
                metrics = []
                count = 0
            metrics.append({
                    'MetricName': name,
                    'Dimensions': [
                        {
                            'Name': 'Resource',
                            'Value': 'RabbitMQ'
                        },
                    ],
                    'Value': messages,
                    'Unit': 'Count',
                    'StorageResolution': 60
                })
            total_messages = total_messages + messages
        if len(metrics) > 0:
            put_metric(metrics)

        put_metric([
                {
                    'MetricName': 'TotalMessages',
                    'Dimensions': [
                        {
                            'Name': 'Resource',
                            'Value': 'RabbitMQ'
                        },
                    ],
                    'Value': total_messages,
                    'Unit': 'Count',
                    'StorageResolution': 60
                },
            ]
        )
        log.info("Total messages: %s", total_messages)
    else:
        log.error('error', resp.status_code)
