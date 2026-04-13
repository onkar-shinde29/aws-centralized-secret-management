from flask import Flask
import boto3
import json
import pymysql

app = Flask(__name__)

def get_secret():
    client = boto3.client("secretsmanager", region_name="ap-south-1")

    response = client.get_secret_value(
        SecretId="prod/db-credentials"
    )

    return json.loads(response["SecretString"])

@app.route("/")
def home():
    secret = get_secret()

    connection = pymysql.connect(
        host="localhost",
        user=secret["username"],
        password=secret["password"],
        database="securedb"
    )

    return "Connected using AWS Secrets Manager"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)