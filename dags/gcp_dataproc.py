import airflow
from airflow import models
from airflow.contrib.operators.dataproc_operator import (
    DataprocClusterCreateOperator,
    DataprocClusterDeleteOperator
)

PROJECT_ID = 'virtual-metrics-368401'
CLUSTER_NAME = 'airflow-cluster'
REGION = 'us-central1'
ZONE = 'us-central1-a'

with models.DAG(
    "Dataproc_create_delete_cluster",
    default_args={"start_date": airflow.utils.dates.days_ago(1)},
    schedule_interval=None,
) as dag:
    create_cluster = DataprocClusterCreateOperator(
        task_id="create_cluster",
        cluster_name=CLUSTER_NAME,
        project_id=PROJECT_ID,
        num_workers=2,
        region=REGION,
    )

    delete_cluster = DataprocClusterDeleteOperator(
        task_id="delete_cluster",
        project_id=PROJECT_ID,
        cluster_name=CLUSTER_NAME,
        region=REGION
    )

    create_cluster >> delete_cluster
