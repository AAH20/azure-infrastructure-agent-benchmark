resource "azurerm_kubernetes_cluster_node_pool" "system" {
  name                  = "system"
  kubernetes_cluster_id = var.cluster_id
  vm_size               = "Standard_D2s_v5"
  enable_auto_scaling   = true
  min_count             = 2
  max_count             = 6
  zones                 = ["1", "2", "3"]
}
