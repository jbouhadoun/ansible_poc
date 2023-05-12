import time 
from dotenv import load_dotenv
import boto3
import os 


#load env
load_dotenv('cloud_ovh.env')
# set s3 client

s3_client = boto3.client("s3", endpoint_url = os.getenv('AWS_S3_ENDPOINT_CLIENT'),aws_access_key_id= os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),region_name='gra')
bucket=os.getenv("AWS_S3_BUCKET") 
test_file='chantiers/D083/2020/dalles_detection_temps.log' 
local_file='/var/tmp/dalles_detection_temps.log'



# Upload test file and measure upload bandwidth
for i in range(6):
    test_file='chantiers/D083/2020/ocsge-gpu'+str(i+1)+'.log'
    local_file='/home/ubuntu/workdir/results/ocsge-gpu'+str(i+1)+'.log'
    start_time = time.time() 
    s3_client.upload_file(local_file, bucket, test_file) 
    end_time = time.time() 
    upload_bandwidth = os.path.getsize(local_file) / (end_time - start_time)
    print(f"Upload bandwidth: {upload_bandwidth} bytes/s")


'''
# Download test file and measure download bandwidth
start_time = time.time() 
s3_client.download_file(bucket, test_file, './modele_down_test.py') 
end_time = time.time() 
download_bandwidth = os.path.getsize(local_file) / (end_time - start_time)
print(f"Download bandwidth: {download_bandwidth} bytes/s")
'''