output "apigw_invoke_url" {
  value = "https://${module.backend_apigw.apigw_id}.apigw.yandexcloud.net"
}

output "ml_external_ip" {
  value = module.ml_cc.external_ip
}
output "ml_internal_ip" {
  value = module.ml_cc.internal_ip
}
