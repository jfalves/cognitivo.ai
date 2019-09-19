#!/usr/bin/env bash

pip install pipenv

pipenv install --dev 

echo "AIRFLOW_HOME=${PWD}/airflow" >> .env

pipenv shell

airflow initdb
mkdir -p ${AIRFLOW_HOME}/dags/
