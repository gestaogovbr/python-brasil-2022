"""
DAG para teste do CopyDbToDb Operator.

Copia dados de tabelas de um banco MySQL para MSSQL e PostgreSQL
"""

from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from FastETL.operators.copy_db_to_db_operator import CopyDbToDbOperator

# Connections

SOURCE_CONN_MYSQL = 'mysql_sample'
DEST_CONN_MSSQL = 'mssql_sample'
DEST_CONN_POSTGRES = 'postgres_sample'

# DAG
default_args = {
    'owner': 'eduardo',
    'start_date': datetime(2022, 10, 14),
    'depends_on_past': False,
    'retries': 0,
    'email_on_failure': False,
}

with DAG(
    'copydbtodb_test',
    default_args=default_args,
    schedule_interval='30 * * * *',
    catchup=False,
    description=__doc__,
    tags=['teste', 'python-brasil']
) as dag:

    # Tasks
    t1 = BashOperator(
        task_id="bash_print_begin",
        bash_command='echo "Iniciando a DAG de cópia de databases"',
        dag=dag
    )

    t2 = CopyDbToDbOperator(
        task_id=f"copy_full_people_MSSQL",
        source_conn_id=SOURCE_CONN_MYSQL,
        source_provider='MYSQL',
        source_table='sampledatabase.People',
        destination_conn_id=DEST_CONN_MSSQL,
        destination_provider='MSSQL',
        destination_table='dbo.People',
        destination_truncate=True,
        dag=dag
    )

    t3 = CopyDbToDbOperator(
        task_id=f"copy_full_people_PG",
        source_conn_id=SOURCE_CONN_MYSQL,
        source_provider='MYSQL',
        source_table='sampledatabase.People',
        destination_conn_id=DEST_CONN_POSTGRES,
        destination_provider='PG',
        destination_table='public.people',
        destination_truncate=True,
        dag=dag
    )

    t1 >> [t2, t3]