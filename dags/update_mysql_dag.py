"""
DAG Hello World
"""

from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator

# Connections
SOURCE_CONN_MYSQL = 'mysql_sample'


# DAG
default_args = {
    'owner': 'devname',
    'start_date': datetime(2022, 10, 14),
    'depends_on_past': False,
    'retries': 0,
    'email_on_failure': False,
}

with DAG(
    'update_mysql_database',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description=__doc__,
    tags=['teste', 'python-brasil']

) as dag:

    # Tasks
    t1 = MySqlOperator(
        task_id="update_mysql",
        sql='UPDATE People SET Company="Python-Brasil";',
        mysql_conn_id=SOURCE_CONN_MYSQL,
        dag=dag
    )
