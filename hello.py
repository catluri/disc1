from flask import Flask
app = Flask(__name__)
@app.route("/Helloworld")
def hello():
	return ""

if __name__=="__main__":
	app.run()

