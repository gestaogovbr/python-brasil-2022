"""
DAG para teste do CopyDbToDb Operator.

Copia dados de tabelas de um banco MySQL para MSSQL e PostgreSQL
"""

from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from FastETL.operators.load_gsheet_operator import LoadGSheetOperator

# Connections

GOOGLE_DRIVE_CONN_ID = 'google_api'
GSHEET_METADATA = {
    "spreadsheet_name": "Cars",
    "sheet_name": "Cars_sheet",
    "spreadsheet_id": "1ADCKXsRgcN5zWieMZZPHKMDYvUle2opkS5cGmWlogrg",
    "link": "https://docs.google.com/spreadsheets/d/1ADCKXsRgcN5zWieMZZPHKMDYvUle2opkS5cGmWlogrg/edit#gid=1073937964"
}

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
    'load_gsheet_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description=__doc__,
    tags=['teste', 'python-brasil']
) as dag:

    # Tasks
    t1 = BashOperator(
        task_id="bash_print_begin",
        bash_command='echo "Iniciando a DAG de carga de dados do GSheet"',
        dag=dag
    )

    t2 = LoadGSheetOperator(task_id='load_gsheet_to_mssql',
                            gsheet_conn_id=GOOGLE_DRIVE_CONN_ID,
                            spreadsheet_id=GSHEET_METADATA['spreadsheet_id'],
                            sheet_name=GSHEET_METADATA['sheet_name'],
                            dest_conn_id=DEST_CONN_MSSQL,
                            schema='dbo',
                            table='Cars',
                            column_name_to_add='imported_google_sheets',
                            value_to_add='True',
                            dag=dag)

    t1 >> t2