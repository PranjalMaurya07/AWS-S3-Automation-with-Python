import boto3

#Show all available buckets
def showBuckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

#Create new buckets
def createBucket(s3, bucketName, region):
    s3.create_bucket(
        Bucket=bucketName,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    print('Bucket created successfully')

#Upload files to S3 buckets
def uploadFile(s3, fileLocation, bucketName, keyName):
    data = open(fileLocation,'rb')
    s3.Bucket(bucketName).put_object(Key=keyName, Body=data)
    print("File uploaded successfully")

#Download files from S3 bucket to local
def downloadFile(s3, bucketName, keyName, downloadPath):
    s3.Bucket(bucketName).download_file(keyName, downloadPath)
    print("File downloaded successfully")

#Parameters
bucketName = "" 
region = ""  #example "ap-south-1"
fileLocation = ""
keyName = ""
downloadPath = ""

#Initialize S3 resources
s3 = boto3.resource("s3",region_name=region)

#Operations
createBucket(s3, bucketName, region)
uploadFile(s3,fileLocation,bucketName,keyName)
showBuckets(s3)
downloadFile(s3,bucketName,keyName,downloadPath)
