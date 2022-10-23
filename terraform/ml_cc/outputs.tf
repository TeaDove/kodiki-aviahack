output "external_ip" {
  value = yandex_compute_instance.ml_service.network_interface.0.nat_ip_address
}
output "internal_ip" {
  value = yandex_compute_instance.ml_service.network_interface.0.ip_address
}
