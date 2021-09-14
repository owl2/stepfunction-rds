import boto3
from utils import *


def lambda_handler(event, context):
    client = boto3.client('rds')

    # response = client.describe_db_snapshots(
    #     DBInstanceIdentifier='database-1'
    # )

    response = client.start_export_task(

    )

    print(response)
    

if __name__ == '__main__':
    lambda_handler(None, None)

