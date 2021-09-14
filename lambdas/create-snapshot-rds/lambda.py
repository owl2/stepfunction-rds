import boto3
import os
from utils import *



backup_interval = int(os.getenv('INTERVAL', '24'))
now = datetime.now()
TIMESTAMP_FORMAT = '%Y-%m-%d-%H-%M'

def lambda_handler(event, context):

    client = boto3.client('rds')

    response = client.describe_db_snapshots(
        DBInstanceIdentifier='database-1'
    )

    if requires_backup(backup_interval, response):
        backup_age = now - get_latest_snapshot_ts(response)
        print('Last backup age: ' + str(backup_age))
        print('Launch of the backup for the database: ')

        timestamp_format = now.strftime(TIMESTAMP_FORMAT)
        snapshot_identifier = 'mysnapshot-snapshot-{}'.format(timestamp_format)

        try:
            response = client.create_db_snapshot(
                DBSnapshotIdentifier=snapshot_identifier,
                DBInstanceIdentifier='database-1'
            )
        except Exception:
            print("Error in the backup action")
    
    else: 
        print('No backup required')
    

if __name__ == '__main__':
    lambda_handler(None, None)