# Quick Summary Table

<https://documentation.neutrinos.com/articles/#!pulse-publication/jbpm-postgresql-compatibility-check-faq>

### Quick Summary Table

1. **PostgreSQL Version**
    `SQL: SHOW server_version_num;`
    Pass Criteria: >= 94000 (9.4+)
    Action if Failed: Upgrade PostgreSQL
2. **Isolation Level**
    `SQL: SHOW default_transaction_isolation;`
    Pass Criteria: read committed, repeatable read, or serializable
    Action if Failed: Set default_transaction_isolation in postgresql.conf
3. **Encoding**
    `SQL: SELECT pg_encoding_to_char(encoding) FROM pg_database WHERE datname = current_database();`
    Pass Criteria: UTF8
    Action if Failed: Recreate database with UTF8 encoding
4. **XA Support**
    SQL: `SHOW max_prepared_transactions;`
    Pass Criteria: > 0 (recommended: 100)
    Action if Failed: Set max_prepared_transactions = 100 in postgresql.conf
5. **User Privileges**
    `SQL: SELECT has_database_privilege(current_user, current_database(), 'CREATE'); `
    Pass Criteria: t (true)
    Action if Failed: GRANT ALL ON DATABASE jbpm TO user;
6. **Schema Privileges**
    `SQL: SELECT has_schema_privilege(current_user, 'public', 'CREATE'); `
    Pass Criteria: t (true)
    Action if Failed: GRANT ALL ON SCHEMA public TO user;
7. **Max Connections**
    `SQL: SHOW max_connections; `
    Pass Criteria: >= 50 (recommended: 100)
    Action if Failed: Set max_connections = 100 in postgresql.conf
8. **CLOB Trigger Table**
    `SQL: SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'jbpm_active_clob');`
    Pass Criteria: t (true) - only if using vacuumlo
    Action if Failed: Run postgresql-jbpm-lo-trigger-clob.sql
9. **Hibernate Dialect**
    `SQL: SELECT CASE WHEN current_setting('server_version_num')::int >= 100000 THEN 'PostgreSQL10Dialect' WHEN current_setting('server_version_num')::int >= 94000 THEN 'PostgreSQL94Dialect' ELSE 'PostgreSQLDialect' END; `
    Pass Criteria: Use the returned dialect value
    Action if Failed: Update persistence.xml with correct dialect

### One-Time Compatibility Check Query

Run this single query to check all requirements at once:

```code
SELECT 

  current_setting('server_version') AS version, 

  CASE WHEN current_setting('server_version_num')::int >= 94000 

       THEN 'PASS' ELSE 'FAIL' END AS version_ok, 

  current_setting('default_transaction_isolation') AS isolation, 

  current_setting('max_prepared_transactions') AS xa_transactions, 

  current_setting('max_connections') AS max_conn, 

  pg_encoding_to_char(encoding) AS encoding, 

  has_database_privilege(current_user, current_database(), 'CREATE') AS can_create 

FROM pg_database WHERE datname = current_database();
```

### Hibernate Dialect Reference

**PostgreSQL 10.x and above**: org.hibernate.dialect.PostgreSQL10Dialect


 **PostgreSQL 9.5.x**: org.hibernate.dialect.PostgreSQL95Dialect


 **PostgreSQL 9.4.x**: org.hibernate.dialect.PostgreSQL94Dialect


 **PostgreSQL 9.2.x - 9.3.x**: org.hibernate.dialect.PostgreSQL92Dialect


 **PostgreSQL below 9.2**: org.hibernate.dialect.PostgreSQLDialect

### Important Notes

- Isolation Level: Must be at least READ COMMITTED for jBPM.


 - XA Transactions: Required for JMS executor or Quartz timers.


 - CLOB Trigger: Only needed if using vacuumlo utility.


 - Encoding: UTF8 recommended for proper character support.
