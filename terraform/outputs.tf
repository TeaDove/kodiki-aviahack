output "apigw_invoke_url" {
  value = "https://${module.backend_apigw.apigw_id}.apigw.yandexcloud.net"
}
#output "bucket_url" {
#  value = module.frontend_s3.bucket_url
#}

#output "queue_url" {
#  value = module.sqs.queue_url
#}
