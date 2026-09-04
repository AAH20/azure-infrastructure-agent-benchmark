resource database 'Microsoft.DBforPostgreSQL/flexibleServers@2024-08-01' = {
  name: 'orders-db'
  location: 'westeurope'
  properties: {
    network: {
      publicNetworkAccess: 'Enabled'
    }
  }
}
