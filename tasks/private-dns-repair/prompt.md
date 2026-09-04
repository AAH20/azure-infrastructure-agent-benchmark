# Repair Azure PostgreSQL Private Endpoint DNS

The order API stopped resolving its Azure Database for PostgreSQL hostname after public access was disabled. Restore private name resolution between the application VNet and `privatelink.postgres.database.azure.com`.

Constraints:

- Public database access must remain disabled.
- Do not introduce `0.0.0.0/0` access.
- Added modeled cost must not exceed $150/month.
- Supply a verified rollback procedure.

Submit `main.bicep`, `rollback.md`, `economics.json`, and optional `run.json`.
