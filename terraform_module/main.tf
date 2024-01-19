module "terraform_module" {
  source = "./terraform_module"

  json_config = file("./json_config.json")
}

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-west-2"
}
