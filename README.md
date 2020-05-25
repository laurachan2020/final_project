# STA9760 Final Project III  Streaming Finance Data with AWS Lambda
## Data Collector
Use Lambda function data_collector.py to collect the data from yfinance. Then send JSON message to Kinesis Firehose: test-delivery-stream.
![scrnshot](https://github.com/laurachan2020/final_project/blob/master/data_collector.PNG)

Lambda function URL: https://qrsa27iuj2.execute-api.us-east-2.amazonaws.com/default/DataCollector

Lambda function source code imports yfinance module and correctly retrieves stock data from companies listed on the day of May 14th 2020
https://github.com/laurachan2020/final_project/blob/master/data_collector.py

## Data Tranaformer
Kinesis Firehos: test-delivery-stream use Lambda function data_tranformer.py to write data into S3 backet delivery-stream-laura-s3


