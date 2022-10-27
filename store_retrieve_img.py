'''
Incomplete test file
'''

from google.cloud import storage
import os
storage_client = storage.Client()
my_bucket=storage_client.get_bucket(os.environ['BUCKET_NAME'])
def upload_to_bucket(blob_name, file_path, bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)
    return blob
file_path = r'/home/widad_mogral_endocodelab_com/wikipedia_db_ongcp/widad.png'


def download_file_from_bucket(blob_name, file_path,bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    with open(file_path, 'wb') as f:
        storage_client.download_blob_to_file(blob, f)
    print('Saved')
#upload_to_bucket('widad.png',file_path,my_bucket)
download_file_from_bucket('widad.png',file_path,my_bucket)
