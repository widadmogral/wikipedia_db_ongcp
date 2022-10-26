from google.cloud import storage
import os
storage_client = storage.Client()
my_bucket=storage_client.get_bucket(os.environ['BUCKET_NAME']):wq
