terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}


resource "yandex_storage_bucket" "bucket" {
  bucket = "www.kodiki-hack.ru"
  acl    = "public-read"

  website {
    index_document = "index.html"
    error_document = "error.html"
    routing_rules = <<EOF
[{
    "Condition": {
        "KeyPrefixEquals": "docs/"
    },
    "Redirect": {
        "ReplaceKeyPrefixWith": "documents/"
    }
}]
EOF
  }

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["PUT", "POST", "GET"]
    allowed_origins = ["https://www.kodiki-hack.ru"]
    expose_headers  = ["ETag"]
    max_age_seconds = 3000
  }

  access_key = yandex_iam_service_account_static_access_key.sa-static-key.access_key
  secret_key = yandex_iam_service_account_static_access_key.sa-static-key.secret_key
}

resource "null_resource" "s3_upload" {
  triggers = {
    always_run = "${timestamp()}"
  }

  provisioner "local-exec"{

    command = "aws s3api delete-objects --endpoint-url https://storage.yandexcloud.net --bucket ${yandex_storage_bucket.bucket.bucket} --delete \"$(aws s3api list-object-versions --endpoint-url https://storage.yandexcloud.net --bucket ${yandex_storage_bucket.bucket.bucket} --query '{Objects: Versions[].{Key: Key, VersionId: VersionId}}' --max-items 1000)\""
  }
  provisioner "local-exec" {
    command    = "aws --endpoint-url=https://storage.yandexcloud.net/ s3 cp --recursive ${var.terraform_dir_path}/../frontend s3://${yandex_storage_bucket.bucket.bucket}"
  }
}

resource "yandex_iam_service_account" "sa" {
  folder_id = var.yc_folder_id
  name      = join("-", [var.name_prefix, "bucket-sa"])
}

resource "yandex_resourcemanager_folder_iam_binding" "sa_binding" {
  role      = each.value
  members   = ["serviceAccount:${yandex_iam_service_account.sa.id}"]
  folder_id = var.yc_folder_id
  for_each = {
    "role1" : "storage.editor"
  }
}

resource "yandex_iam_service_account_static_access_key" "sa-static-key" {
  service_account_id = yandex_iam_service_account.sa.id
}
