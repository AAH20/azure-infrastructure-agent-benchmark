resource "azurerm_kubernetes_cluster_node_pool" "system" {
  name                  = "system"
  kubernetes_cluster_id = var.cluster_id
  vm_size               = "Standard_D2s_v5"
  node_count            = 1
}
