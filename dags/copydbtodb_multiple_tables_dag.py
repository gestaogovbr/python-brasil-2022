"""
DAG para teste do CopyDbToDb Operator para múltiplas tabelas

Copia dados de tabelas de um banco MySQL para MSSQL
"""

from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from FastETL.operators.copy_db_to_db_operator import CopyDbToDbOperator

# Connections

SOURCE_CONN_MYSQL = 'mysql_sample'
DEST_CONN_MSSQL = 'mssql_sample'

# DAG
default_args = {
    'owner': 'eduardo',
    'start_date': datetime(2022, 10, 14),
    'depends_on_past': False,
    'retries': 0,
    'email_on_failure': False,
}

with DAG(
    'copydbtodb_multiple_tables_test',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description=__doc__,
    tags=['teste', 'python-brasil']
) as dag:

    # Função para carga FULL das tabelas
    def copy_full(table: str, SOURCE_SCHEMA: str, DEST_SCHEMA: str):
        "Realiza a carga full da tabela (table)."

        CopyDbToDbOperator(
            task_id=f"copy_full_{table}",
            destination_table=f"{DEST_SCHEMA}.{table}",
            source_conn_id=SOURCE_CONN_MYSQL,
            source_provider='MYSQL',
            destination_conn_id=DEST_CONN_MSSQL ,
            destination_provider='MSSQL',
            source_table=f"{SOURCE_SCHEMA}.{table}",
            destination_truncate=True,
            dag=dag
        )


    copy_full(table='People', SOURCE_SCHEMA='sampledatabase', DEST_SCHEMA='dbo')
    copy_full(table='Movie', SOURCE_SCHEMA='sampledatabase', DEST_SCHEMA='dbo')

