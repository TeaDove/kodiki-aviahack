terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}


module "backend_lambda" {
  source = "./backend_lambda"

  yc_folder_id       = var.yc_folder_id
  is_prod            = var.is_prod
  log_level          = var.log_level
  name_prefix        = var.name_prefix
  terraform_dir_path = var.terraform_dir_path

  show_swagger     = var.show_swagger
}

module "backend_apigw" {
  source = "./backend_apigw"

  function_id                 = module.backend_lambda.function_id
  function_service_account_id = module.backend_lambda.service_account_id
  name_prefix                 = var.name_prefix
}

module "vpc" {
  source = "./vpc"

  name_prefix = var.name_prefix
}

module "ml_cc" {
  source = "./ml_cc"

  terraform_dir_path = var.terraform_dir_path
  internal_ip_address = var.ml_internal_ip_address
  vpc_subnet_id = module.vpc.vpc_subnet_id
  name_prefix = var.name_prefix
  yc_folder_id = var.yc_folder_id
}
