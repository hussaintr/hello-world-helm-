import airflow
from airflow import DAG
from airflow.utils.dates import days_ago


from airflow.contrib.operators.dataproc_operator import (
    DataprocClusterCreateOperator,
    DataProcPySparkOperator,
    DataprocClusterDeleteOperator,
)


default_arguments = {"owner": "Put your name", "start_date": days_ago(1)}


with DAG(
    "check-Min-temp",
    schedule_interval="0 20 * * *",
    catchup=False,
    default_args=default_arguments,
) as dag:
    create_cluster=DataprocClusterCreateOperator(
        task_id='create_cluster',
        project_id='virtual-metrics-368401',
        cluster_name='spark-cluster-{{ds_nodash}}',
        num_workers=2,
        worker_machine_type='n1-standard-2',
        storage_bucket="dataproc-pyspark-bucket",
        region="us-central1"
        zone="us-central1-a",
    )


    calculate_min_temp=DataProcPySparkOperator(
        task_id='calculate_min_temp',
        main='gs://[GCS Bucket]/dataproc.py',
        arguments=['gs://[input file path]','gs://[output file path]/output'],
        cluster_name="spark-cluster-{{ ds_nodash }}",
        dataproc_pyspark_jars="gs://spark-lib/bigquery/spark-bigquery-latest.jar",
    )


    delete_cluster=DataprocClusterDeleteOperator(
        task_id="delete_cluster",
        project_id="beam-290211",
        cluster_name="spark-cluster-{{ ds_nodash }}",
        trigger_rule="all_done",
    )



create_cluster>>calculate_min_temp>>delete_cluster
