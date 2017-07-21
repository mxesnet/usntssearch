# ./appTest.py
from flask import Flask
appTest = Flask(__name__)
@app.route('/')
def index():
	return 'Yo, its working!'
if __name__ == "__main__":
	from os import environ
	appTest.run(debug=True, host='0.0.0.0', port=int(environ.get("PORT", 5000)))
