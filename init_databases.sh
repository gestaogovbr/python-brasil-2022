# Create database for Sql Server
docker cp ./database_samples/mssql_database_example.sql mssqlserver:/tmp/mssql_database_example.sql
docker exec -it mssqlserver sh -c "/opt/mssql-tools/bin/sqlcmd -S mssqlserver -U sa -P python@mssql17! -d master -i /tmp/mssql_database_example.sql"

# Create database for Postgres
docker cp ./database_samples/postgres_database_example.sql postgres13:/tmp/postgres_database_example.sql
docker exec -it postgres13 sh -c "psql -U airflow -f /tmp/postgres_database_example.sql"

# Create database for Mysql
docker cp ./database_samples/mysql_database_example.sql mysql8:/tmp/mysql_database_example.sql
docker exec -it mysql8 sh -c "mysql -u root --password=S3cret < /tmp/mysql_database_example.sql"