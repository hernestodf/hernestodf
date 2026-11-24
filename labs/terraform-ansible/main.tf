terraform {
  required_version = ">= 1.4.0"
}
resource "terraform_data" "demo" {
  input = {
    servico = "portal-demo"
    ambiente = "laboratorio"
  }
}
output "configuracao" {
  value = terraform_data.demo.output
}
