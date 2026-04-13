from flask import Flask
import pymysql

app = Flask(__name__)

@app.route("/")
def home():
    connection = pymysql.connect(
        host="localhost",
        user="appuser",
        password="Password@123",  
        database="securedb"
    )
    return "Connected using HARDCODED password "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)