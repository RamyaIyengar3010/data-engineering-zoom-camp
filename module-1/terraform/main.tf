terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "8.12.0"
    }
  }
}

provider "google" {
  project = "future-lane-514608-g3"
  region  = "us-central1"
}


resource "google_storage_bucket" "demo-gcs-bucket" {
  name          = "future-lane-514608-g3-demo-gcs-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
