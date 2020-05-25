import boto3
import json
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')
import yfinance as yf

stocks = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']


def lambda_handler(event, context):
    fh = boto3.client("firehose", "us-east-2")
    delivery_system_name = "test-delivery-stream"
    for stock in stocks:
        stock_data = yf.Ticker(stock).history(start="2020-05-14", end="2020-05-15", interval="1m")
        for index, row in stock_data.iterrows():
            data = {"high": row.High, "low": row.Low, "ts": str(index), "name": stock}
            as_jsonstr = json.dumps(data)
            fh.put_record(
                DeliveryStreamName="test-delivery-stream",
                Record={"Data": as_jsonstr.encode('utf-8')})

    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Sending Records to {delivery_system_name}')
    }
