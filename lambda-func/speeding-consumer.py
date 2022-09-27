import base64

def lambda_handler(event, context):
    for record in event["Records"]:
        decoded_data = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
        print(decoded_data)