# terraform_sample: Provision a simple AWS S3 bucket and security group baseline.
terraform {
  required_version = ">= 1.3"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "Unique S3 bucket name"
  type        = string
}

resource "aws_s3_bucket" "app" {
  bucket = var.bucket_name
  tags = {
    Name = "app-artifacts"
  }
}

resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Allow HTTP ingress"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "web-sg"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.app.bucket
}
