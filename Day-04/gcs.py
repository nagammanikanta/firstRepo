from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "mykey.json"

project_id = 'data-rainfall-396303'
bucket_name = 'bkt-dev-006'

storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
bucket.location = 'us'
bucket.create(project=project_id,location="us")
print(f'Bucket {bucket_name} created.')


