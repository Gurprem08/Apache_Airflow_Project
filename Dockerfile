FROM apache/airflow:2.7.1-python3.9

# Copy the requirements.txt file into the container
COPY requirements.txt /opt/airflow/requirements.txt

USER root
RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt