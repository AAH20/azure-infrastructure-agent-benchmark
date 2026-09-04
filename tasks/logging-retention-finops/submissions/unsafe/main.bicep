resource workspace 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: 'log-production'
  location: 'westeurope'
  properties: { retentionInDays: 7 }
}
