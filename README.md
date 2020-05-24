# STA9760 Final Project III  Streaming Finance Data with AWS Lambda
## Data Collector
Use Lambda function data_collector.py to collect the data from yfinance. Then send JSON message to Kinesis Firehose: test-delivery-stream.
https://github.com/laurachan2020/final_project/blob/master/data_collector.PNG

## Data Tranaformer
Kinesis Firehos: test-delivery-stream use Lambda function data_tranformer.py to write data into S3 backet delivery-stream-laura-s3


