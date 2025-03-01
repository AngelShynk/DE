from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define a simple Python function
def print_hello():
    print("Hello, Airflow! This is a simple Python task.")

# Define default arguments for the DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 3, 1),  # Start running from this date
}

# Define the DAG
dag = DAG(
    "simple_python_dag",   # DAG Name
    default_args=default_args,
    schedule_interval="0 9 * * *",  # Run daily at 9 AM
    catchup=False
)

# Define the task using PythonOperator
hello_task = PythonOperator(
    task_id="print_hello_task",
    python_callable=print_hello,
    dag=dag
)

# Set task execution order (only one task in this case)
hello_task
