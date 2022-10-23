output "apigw_invoke_url" {
  value = "https://${module.backend_apigw.apigw_id}.apigw.yandexcloud.net"
}
