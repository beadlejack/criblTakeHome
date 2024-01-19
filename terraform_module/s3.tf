locals {
  buckets = jsondecode(file(var.json_config))["buckets"]
}

# declare the bucket
resource "aws_s3_bucket" "buckets" {
  count = length(local.buckets)
  bucket = local.buckets[count.index].name
}

# add logging to the bucket
resource "aws_s3_bucket_logging" "logging" {
  count = length(local.buckets)
  bucket = local.buckets[count.index].name
  target_bucket = 'cribl-s3-logs'
  target_prefix = 'log/' + local.buckets[count.index].name + '/'
}

# add version to the bucket
resource "aws_s3_bucket_versioning" "versioning" {
  count = length(local.buckets)
  bucket = local.buckets[count.index].name
  versioning_configuration {
    status = 'Enabled'
  }
}
