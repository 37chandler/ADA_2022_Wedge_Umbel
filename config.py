"""BigQuery Configuration."""
from os import environ


# Google BigQuery config

gcp_credentials = environ.get('GCP_CREDENTIALS')
gcp_project = environ.get('GCP_PROJECT')
bigquery_dataset = environ.get('GCP_BIGQUERY_DATASET')
bigquery_table = environ.get('GCP_BIGQUERY_TABLE')
bigquery_uri = 'bigquery://dakota-umt-msba/umt_msba'


