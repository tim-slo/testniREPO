from flask import Flask, render_template, request
import random
#pip install flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/calcLove", methods = ["POST"])
def calcLove():
    
    d = request.form
    ime1 =d.get("ime1").lower()
    ime2 =d.get("ime2").lower()
    a1= 0
    a2= 0
    for i in ime1 :
        a1+=1
    for i in ime2 :
        a2+=1

    if a1 == 0:
        rez = f"{ime1} + {ime2} = {0} %"
    elif a2 == 0:
       rez = f"{ime1} + {ime2} = {0} %" 
    if ime1 or ime2 == "tim":
        rez = f"{ime1} + {ime2} = {random.randint(90,100)} %"

    else:
        rez = f"{ime1} + {ime2} = {random.randint(0,100)} %"
    return render_template("index.html", rez=rez)
    #return <img src="img.jpg" alt="" width="500" height="600">

    

app.run(debug = True)