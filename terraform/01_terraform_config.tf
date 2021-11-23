// Terraform configuration
terraform {
  required_version = ">= 1.0.2, < 2.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}