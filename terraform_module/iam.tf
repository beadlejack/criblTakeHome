locals {
  roles = jsondecode(file(var.json_config))["roles"]
}

resource "aws_iam_role" "iam_roles" {
  count    = length(local.roles)
  name     = local.roles[count.index].name
  assume_role_policy = local.roles[count.index].assume_role_policy
  # Add other IAM role configurations as needed
}
