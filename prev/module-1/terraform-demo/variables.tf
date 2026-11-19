variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my-cred.json"
}

variable "project" {
  description = "Project"
  default     = "project-72fe43c8-cf88-4f6a-93d"
}

variable "region" {
  description = "Project Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My big query dataset name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket name"
  default     = "terra-bucket-72fe43c8-cf88-4f6a-93d"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"

}