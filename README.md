# STA9760 Final Project III  Streaming Finance Data with AWS Lambda
## Data Collector
Use Lambda function data_collector.py to collect the data from yfinance. Then send JSON message to Kinesis Firehose: test-delivery-stream.

Lambda function URL: https://qrsa27iuj2.execute-api.us-east-2.amazonaws.com/default/DataCollector

Lambda function source code imports yfinance module and correctly retrieves stock data from companies listed on the day of May 14th 2020
https://github.com/laurachan2020/final_project/blob/master/data_collector.py


DataCollector Lambda configuration page
![scrnshot](https://github.com/laurachan2020/final_project/blob/master/resources/data_connector_lambda_configuration.PNG)

## Data Tranaformer
Kinesis Firehos: test-delivery-stream use Lambda function data_tranformer.py to write data into S3 backet delivery-stream-laura-s3

Lambda function calls boto3.client(‘firehose’) to put records successfully into the firehose delivery stream:
https://github.com/laurachan2020/final_project/blob/master/data_transformer.py

Kinesis Data Firehose Delivery Stream Monitoring
![scrnshot](https://github.com/laurachan2020/final_project/blob/master/resources/kinesis_firehose_delivery_system_monitoring.PNG)

## DataAnalyzer

Highest hourly stock “high” per company from the list provided

['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']

Athena query file
https://github.com/laurachan2020/final_project/blob/master/query.sql

Query output file
https://github.com/laurachan2020/final_project/blob/master/result.csv


## Extra Credit

https://github.com/laurachan2020/final_project/blob/master/Analysis.ipynb


