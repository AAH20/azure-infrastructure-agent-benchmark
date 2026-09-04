param applicationVnetName string

resource applicationVnet 'Microsoft.Network/virtualNetworks@2024-05-01' existing = {
  name: applicationVnetName
}

resource privateZone 'Microsoft.Network/privateDnsZones@2024-06-01' = {
  name: 'privatelink.postgres.database.azure.com'
  location: 'global'
}

resource applicationLink 'Microsoft.Network/privateDnsZones/virtualNetworkLinks@2024-06-01' = {
  parent: privateZone
  name: 'order-api-link'
  location: 'global'
  properties: {
    registrationEnabled: false
    virtualNetwork: {
      id: applicationVnet.id
    }
  }
}
