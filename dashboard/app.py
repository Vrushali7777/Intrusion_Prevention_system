from flask import Flask,render_template

app = Flask(__name__)

logfile = "../logs/attacks.log"

@app.route("/")

def home():

    logs=[]

    try:

        with open(logfile) as f:
            logs=f.readlines()

    except:
        logs=[]

    return render_template("index.html",logs=logs)

app.run()