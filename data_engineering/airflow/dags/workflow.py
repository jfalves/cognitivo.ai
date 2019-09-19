from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

default_args = {
   'owner': 'jonathan_alves',
   'depends_on_past': False,
   'start_date': datetime(2019, 9, 18),
   'retries': 0,
   }

with DAG(
   'project-workflow',
   schedule_interval=timedelta(minutes=10),
   catchup=False,
   default_args=default_args
   ) as dag:
   task1 = BashOperator(
      task_id='price_quote',
      bash_command="""
      cd $AIRFLOW_HOME/../
      python3 etl_price_quote.py
      """)
   task2 = BashOperator(
      task_id='comp_boss',
      bash_command="""
      cd $AIRFLOW_HOME/../
      python3 etl_comp_boss.py
      """)
   task3 = BashOperator(
      task_id='bill_of_materials',
      bash_command="""
      cd $AIRFLOW_HOME/../
      python3 etl_bill_of_materials.py
      """)

task1 >> task2 >> task3
