from flask import Flask, render_template, request, flash
import os
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

app.config["UPLOAD_FOLDER"] = os.path.join("static","images")
pic = os.path.join(app.config["UPLOAD_FOLDER"],"angel.jpeg")
@app.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html",pic1=pic)

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html",pic1=pic)

if __name__=="__main__":
	app.run(debug=True)