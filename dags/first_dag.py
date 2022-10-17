"""
DAG de teste
"""

from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import PythonOperator

# DAG
default_args = {
    'owner': 'devname',
    'start_date': datetime(2022, 10, 14),
    'depends_on_past': False,
    'retries': 0,
    'email_on_failure': False,
}

with DAG(
    'bash_test',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description=__doc__,
    tags=['teste', 'python-brasil']
) as dag:

    def print_example():

        print ("Teste com Python Operator")

    # Tasks
    t1 = BashOperator(
        task_id="bash_print",
        bash_command='echo "Teste com Bash Operator"',
        dag=dag
    )

    t2 = PythonOperator(
        task_id="python_print",
        python_callable=print_example,
        dag=dag
    )

    # Orquestração
    t1 >> t2
