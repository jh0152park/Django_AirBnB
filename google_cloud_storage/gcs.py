import os
import urllib.request
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

storage_client = storage.Client()
# print(dir(storage_client))

"""
Get a bucket from Google Cloud Storage
"""
bucket_name = "airbnb_study"
bucket = storage_client.bucket(bucket_name)

"""
Create a new bucket
"""
# bucket_name = [my new bucket name] and it also have to be unique
# bucket = storage_client.bucket(bucket_name)
# bucket.location = "KR" / "US"
# bucket = storage_client.create_bucket(bucket_name)

"""
Bucket Details
"""
# print(vars(bucket))

"""
Access to specific bucket
"""
my_bucket = storage_client.get_bucket(bucket_name)
# print(vars(my_bucket))

"""
Upload files
"""


# BLOB: A Binary Large OBject is a collection of binary data stored as a single entity.
def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)

        # image url upload
        file = urllib.request.urlopen(file_path)
        blob.upload_from_string(file.read())

        # local file upload
        # blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print("\n\nOccurred some error as below.")
        print(e)
        print("\n\n")
        return False


# local file upload
# amg_file_path = r"/Users/parkjaehyeon/Desktop/Study/Programming/Django/Django_AirBnB/google_cloud_storage/amg_gt.jpg"
# rr_file_path = r"/Users/parkjaehyeon/Desktop/Study/Programming/Django/Django_AirBnB/google_cloud_storage/RR.jpg"
# upload_to_bucket("amg_gt", amg_file_path, bucket_name)
# upload_to_bucket("rr2", rr_file_path, bucket_name)

# image url upload
# bentley = "https://images.unsplash.com/photo-1471289549423-04adaecfa1f1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTF8fGx1eHVyeSUyMGNhcnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60"
# upload_to_bucket("bentley", bentley, bucket_name)

"""
Download files
"""


def download_file_from_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        with open(file_path, "wb") as f:
            storage_client.download_blob_to_file(blob, f)

        return True
    except Exception as e:
        print("\n\nOccurred some error as below.")
        print(e)
        print("\n\n")
        return False


def get_public_url(bucket_name, file_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    return blob.generate_signed_url(expiration=3600)


# download_file_from_bucket("bentley", os.path.join(os.getcwd(), "beny.jpg"), bucket_name)

# public url
# https://storage.googleapis.com/[bucket]/[object]
# https://storage.googleapis.com/airbnb_study/bentely
# https://storage.cloud.google.com/airbnb_study/rr2
