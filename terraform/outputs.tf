output "ecr_repo_url" {
  description = "ECR repository URL"
  value       = aws_ecr_repository.mlops_repo.repository_url
}

output "s3_bucket_name" {
  description = "S3 bucket for model and MLflow artifacts"
  value       = aws_s3_bucket.mlops_artifacts.bucket
}

output "eks_cluster_name" {
  description = "EKS cluster name"
  value       = module.eks.cluster_name
}