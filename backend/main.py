from flask import Flask
import pandas as pd

app=Flask(__name__)
@app.route("/products",methods=['GET'])
def read_data():
	df=pd.read_csv("products.csv")
	json_data=df.to_json()
	return json_data
if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5001)
