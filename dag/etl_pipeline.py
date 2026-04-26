from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Add script path
sys.path.append(os.path.join(os.path.dirname(__file__), "../scripts"))

from transform import transform

default_args = {
    "owner": "varun",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

with DAG(
    dag_id="etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform
    )

    transform_task
