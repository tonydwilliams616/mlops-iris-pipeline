variable "project" {
  description = "Project name"
  type        = string
  default     = "mlops-iris"
}

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "vpc_id" {
  description = "Existing VPC ID for EKS cluster"
  type        = string
}

variable "subnet_ids" {
  description = "Subnets for EKS worker nodes"
  type        = list(string)
}