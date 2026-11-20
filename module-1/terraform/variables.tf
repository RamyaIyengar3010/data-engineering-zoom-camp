variable "credentials" {
  description = "My credentials"
  default = "./keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default = "future-lane-514608-g3"
}

variable "region" {
  description = "Project region"
  default = "us-central1"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset"
  default = "demo_dataset"
}

variable "location" {
  description = "Location"
  default = "EU"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default = "future-lane-514608-g3-demo-gcs-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket storage class"
  default = "STANDARD"
}
