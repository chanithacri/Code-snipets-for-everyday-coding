-- backup_restore: Backup/restore commands (vendor notes).
-- Always test restore scripts; never overwrite production without snapshots.

-- Postgres: full plain-text backup and restore
-- pg_dump -U $USER -h localhost -d shop > shop.sql
-- psql -U $USER -h localhost -d shop < shop.sql

-- Postgres: compressed custom format
-- pg_dump -U $USER -h localhost -F c -b -v -f shop.backup shop
-- pg_restore -U $USER -h localhost -d shop -v shop.backup

-- MySQL: logical backup
-- mysqldump -u $USER -p --databases shop > shop.sql
-- mysql -u $USER -p shop < shop.sql

-- SQLite: single-file copy (hot backups use .backup command)
-- sqlite3 shop.db ".backup 'shop-backup.db'"
