import time 
from dotenv import load_dotenv
import boto3
import os 
import tqdm

#load env
load_dotenv('cloud_ovh.env')
# set s3 client

s3_client = boto3.client("s3", endpoint_url = os.getenv('AWS_S3_ENDPOINT_CLIENT'),aws_access_key_id= os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),region_name='gra')
bucket=os.getenv("AWS_S3_BUCKET") 
'''
test_file='chantiers/D083/2020/modeles/D083_2020_UNET_FEV11/odeon_val_loss_ckpt/D083_2020_UNET_FEV11_version_name/D083_2020_UNET_FEV11.ckpt' 
local_file='./modele.ckpt'



# Upload test file and measure upload bandwidth
start_time = time.time() 
s3_client.upload_file(local_file, bucket, test_file) 
end_time = time.time() 
upload_bandwidth = os.path.getsize(local_file) / (end_time - start_time)
print(f"Upload bandwidth: {upload_bandwidth} bytes/s")



# Download test file and measure download bandwidth
start_time = time.time() 
s3_client.download_file(bucket, test_file, './modele_down_test.py') 
end_time = time.time() 
download_bandwidth = os.path.getsize(local_file) / (end_time - start_time)
print(f"Download bandwidth: {download_bandwidth} bytes/s")
'''
prefix = 'chantiers'
bucket_name = os.getenv("AWS_S3_BUCKET")

def list_all_objects(s3_client, bucket_name, prefix):
    paginator = s3_client.get_paginator('list_objects_v2')
    response_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

    all_objects = []
    print("la")
    for response in response_iterator:
        for obj in response['Contents']:
            if "mns" in obj['Key']:
                all_objects.append(obj['Key'])

    return all_objects


base_directory='/var/data/store-ocsge/'
files = list_all_objects(s3_client, bucket_name, prefix)
start_time = time.time() 
for file in tqdm.tqdm(files):
    # Créez l'arborescence des dossiers en local
    local_path = os.path.join(base_directory, file)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    # Téléchargez le fichier à partir du bucket S3
    s3_client.download_file(bucket_name, file, local_path)
    
end_time = time.time() 
download_bandwidth =  (end_time - start_time)
print(f"Download bandwidth: {download_bandwidth} s")

