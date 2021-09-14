import boto3
from datetime import datetime
import re

class SnapshotToolException(Exception):
    pass


def get_latest_snapshot_ts(response):
# Get lastest snapshot for a specific DBInstanceIdentifier
    timestamps = []

    for snapshot in response['DBSnapshots']:
        timestamp = snapshot['SnapshotCreateTime']

        if timestamp is not None: 
            timestamps.append(timestamp.replace(tzinfo=None))

    if len(timestamps) > 0:
        return max(timestamps)
    else:
        return None


def requires_backup(backup_interval, snapshotIdentifier):
# Return True  if the latest Snapshot is older than the interval
    latest = get_latest_snapshot_ts(snapshotIdentifier)

    if latest is not None:
        backup_age = datetime.now() - latest

        if backup_age.total_seconds() >= (backup_interval * 60 * 60):
            return True
        else: 
            return False
    elif latest is None:
        return True
    else:
        print("Error in the requires_backup function")