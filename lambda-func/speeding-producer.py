import datetime
import json
import random
import boto3
import time
import string
import os

STREAM_NAME = os.environ['streamname']

def lambda_handler(event, context):
    generate(STREAM_NAME, boto3.client('kinesis'))

def get_data():
    return {
        'EVENT_TIME': datetime.datetime.now().isoformat(),
        'BRAND': random.choice(['Honda', 'Ford', 'Toyota', 'Tesla', 'Audi', 'BMW', 'Nissan', 'Mazda']),
        'PLATE': random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + '-' + str(round(random.random() * 1000)),
        'SPEED': round(random.random() * 200, 2)}


def generate(stream_name, kinesis_client):
    i = 1
    while i < 10:
        data = get_data()
        print(data)
        time.sleep(0.1)
        kinesis_client.put_record(
             StreamName=stream_name,
             Data=json.dumps(data),
             PartitionKey="partitionkey")
        i += 1