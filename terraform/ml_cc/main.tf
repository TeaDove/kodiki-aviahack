terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

data "yandex_compute_image" "container-optimized-image" {
  family = "ubuntu-2004-lts"
}

resource "yandex_compute_instance" "ml_service" {
  name        = join("-", [var.name_prefix, "ml-service"])
  platform_id = "standard-v3"


  resources {
    cores         = 8
    memory        = 8
    core_fraction = 100
  }

  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.container-optimized-image.id
      size = 50
    }
  }

  network_interface {
    ip_address = var.internal_ip_address
    subnet_id  = var.vpc_subnet_id
    nat        = true
  }

  service_account_id = yandex_iam_service_account.sa.id

  metadata = {
    user-data = file("${var.terraform_dir_path}/ml_cc/user-data.yml")
  }

  scheduling_policy {
    preemptible = true
  }
}

resource "yandex_iam_service_account" "sa" {
  name = join("-", [var.name_prefix, "sa"])
}

resource "yandex_resourcemanager_folder_iam_binding" "sa_binding" {
  role      = each.value
  members   = ["serviceAccount:${yandex_iam_service_account.sa.id}"]
  folder_id = var.yc_folder_id
  for_each = {
    "role1" : "container-registry.images.puller"
  }
}
