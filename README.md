Data Pipeline with Reddit, Airflow, Celery, Postgres, S3, AWS Glue, Athena, and Redshift

This project offers a complete data pipeline solution to extract, transform, and load (ETL) Reddit data into a Redshift data warehouse. The pipeline utilizes a variety of tools and services including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.

Overview
The pipeline is designed to:

Extract data from Reddit using its API.
Store the raw data into an S3 bucket from Airflow.
Transform the data using AWS Glue and Amazon Athena.
Load the transformed data into Amazon Redshift for analytics and querying.

Architecture

Reddit API: The source of the data.
Apache Airflow & Celery: Orchestrates the ETL process and manages task distribution.
PostgreSQL: Temporary storage and metadata management.
Amazon S3: Storage for raw data.
AWS Glue: Data cataloging and ETL jobs.
Amazon Athena: SQL-based data transformation.
Amazon Redshift: Data warehousing and analytics.

Prerequisites

AWS Account with permissions for S3, Glue, Athena, and Redshift.
Reddit API credentials.
Docker installed.
Python 3.9 or higher.