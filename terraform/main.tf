terraform {
  required_version = ">= 1.12.1"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.region
}

# ------------------------------------------
# S3 Bucket for MLflow artifacts / model store
# ------------------------------------------
resource "aws_s3_bucket" "mlops_artifacts" {
  bucket        = "${var.project}-artifacts-${random_id.suffix.hex}"
  force_destroy = true
  tags = {
    Project = var.project
    Purpose = "mlflow-artifacts"
  }
}

resource "random_id" "suffix" {
  byte_length = 4
}

# ------------------------------------------
# ECR Repository for Docker Images
# ------------------------------------------
resource "aws_ecr_repository" "mlops_repo" {
  name                 = "${var.project}-repo"
  image_tag_mutability = "MUTABLE"
  force_delete         = true
}

# ------------------------------------------
# EKS Cluster (simplified)
# ------------------------------------------
module "eks" {
  source      = "terraform-aws-modules/eks/aws"
  name        = "${var.project}-eks"
  version     = "~> 21.0"
  vpc_id      = var.vpc_id
  subnet_ids  = var.subnet_ids
  enable_irsa = true

  tags = {
    Project = var.project
  }
}