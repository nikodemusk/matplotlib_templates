# See also:
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
# and
# https://docs.aws.amazon.com/code-samples/latest/catalog/python-s3-s3-python-example-upload-file.py.html

import os
import magic
from boto3 import session
from botocore.client import Config

ACCESS_ID = os.environ['AWS_ACCESS_KEY_ID']
SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
URL = 'https://nyc3.digitaloceanspaces.com'
bucket = os.environ['GRAPH_BUCKET']
region_name = os.environ['REGION_NAME']

mime = magic.Magic(mime=True)

#Initiate session
session = session.Session()
client = session.client('s3',
                        region_name           = region_name,
                        endpoint_url          = URL,
                        aws_access_key_id     = ACCESS_ID,
                        aws_secret_access_key = SECRET_KEY)

def upload(name, localPath, remotePath):
   mimeType = mime.from_file(str(localPath + name))
   client.upload_file(str(localPath + name), bucket,
                      remotePath + name,
                      ExtraArgs={'ACL': 'public-read',
                                 'ContentType': mime.from_file(localPath + name),
                                 'CacheControl': 'no-cache'})
   return(f"https://{bucket}.{region_name}.digitaloceanspaces.com/{remotePath}{name}")
