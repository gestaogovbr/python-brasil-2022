"""
DAG de leitura de um banco MySQL imprimindo um resultado na tela, utilizando Hooks
"""

from datetime import datetime
from airflow import DAG
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.operators.python import PythonOperator
from airflow.operators.email_operator import EmailOperator
import logging


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
    'read_mysql_xcom_send_mail',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description=__doc__,
    tags=['teste', 'python-brasil']

) as dag:

    def return_sql():
        mysql_hook = MySqlHook(SOURCE_CONN_MYSQL)
        sql = "SELECT count(*) from People;"
        row_count = mysql_hook.get_records(sql)
        return (row_count[0][0])
 

    # Tasks
    t1 = PythonOperator(
        task_id="select_mysql_xcom",
        python_callable=return_sql,
        provide_context=True,
        dag=dag
    )

    t2 = EmailOperator(
        task_id='send_email',
        to='airflow@domain.com',
        subject='Query Result',
        html_content="<b><h1> {{ task_instance.xcom_pull(task_ids='select_mysql_xcom') }} Registros na tabela </h1></b>",
        dag=dag
    )

    t1 >> t2