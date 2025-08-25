
# AWS S3 Automation with Python

This project demonstrates how to automate AWS S3 operations using Python and boto3.
# Features

- Create an S3 bucket
- Upload files to S3
- List all available buckets
- Download files from S3



    


# Prerequisites


- Python 3.8+
- AWS Account with S3 access
- AWS CLI installed & configured

### bash

```bash
  aws configure
```

```bash
  Enter your AWS Access Key, Secret Key, Region (e.g., ap-south-1), and output format.
```
# Installation

```bash
  git clone https://github.com/<your-username>/aws-s3-automation.git
```
```bash
  pip install boto3
```
```bash
  cd aws-s3-automation
```
# Usage

### Create a bucket

##### from s3_backup import createBucket 
##### import boto3
##### s3 = boto3.resource("s3",region_name="ap-south-1")
##### createBucket(s3, bucketName, region)

### Upload a File

##### from s3_backup import uploadFile
##### import boto3
##### s3 = boto3.resource("s3", region_name="ap-south-1")
##### uploadFile(s3,fileLocation,bucketName,keyName)

### Show all buckets

##### from s3_backup import showBuckets
##### import boto3
##### s3 = boto3.resource("s3", region_name="ap-south-1")
##### showBuckets(s3)

### Download File

##### from s3_backup import downloadFile
##### import boto3
##### s3 = boto3.resource("s3", region_name=region)
##### downloadFile(s3,bucketName,keyName,downloadPath)

# Contacts

- Name : Pranjal Kumar Maurya
- Email : pranjalmaurya003@gmail.com
- Github : https://github.com/PranjalMaurya07
- LinkedIn : https://www.linkedin.com/in/pranjalmaurya07/
