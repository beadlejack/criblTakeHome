Jackson Beadle
January 19, 2024
Take Home Assessment
Data Engineer -- Cribl

Question 1 -- Terraform Module

Disclosure: I do not have exposure to Terraform. In my previous role, we used a mix of Serverless,
CloudFormation templates, and CDK to deploy infrastructure within our AWS data ecosystem. This is my
first attempt to create a Terraform module. I used ChatGPT to gain an understanding of how my files
should be structured and referred to Terraform's documentation on resources constructs.

Attempted functionality: This module will (hopefully) deploy a set of S3 buckets and IAM roles as
defined in json_config.json. The buckets have access logging and versioning enabled, with logs going
to a generic "cribl-s3-logs" bucket under a prefix that matches the bucket name. The IAM roles are to
grant read/write/delete/list permissions to each bucket.
