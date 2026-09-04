resource workspace 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: 'log-production'
  location: 'westeurope'
  properties: {
    retentionInDays: 60
    workspaceCapping: {
      dailyQuotaGb: 2
    }
    sku: { name: 'PerGB2018' }
    features: { enableLogAccessUsingOnlyResourcePermissions: true }
  }
}
