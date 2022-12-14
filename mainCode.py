from flask import Flask, render_template, url_for, request, redirect
from subprocess import PIPE, STDOUT, run
from flask_sqlalchemy import SQLAlchemy
from serverDB import Flask, app, Info, server_db

"""  app variable is a Flask object imported from serverDB file where it was created.
With this website, you can code in the textbox and run, save and  
 
 
 
 
 """
global runClickCounter
runClickCounter =0


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")




@app.route("/run_code", methods=['POST', 'GET'])
def run_code():
    global runClickCounter
    if request.method == 'POST':

        code = request.form['codeHere']
        p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
        output = p.stdout
        runClickCounter =+ 1
        return render_template("index.html", print_output=output, codearea=code, runClickCounter_=runClickCounter)
    else:
        return render_template("index.html")



@app.route("/save_code", methods=["GET", "POST"])
def add_code():
    if request.method == "POST":

        code = request.form['codeHere']
        Info.revertSuccesfulCode= code
        server_db.session.commit()

        return render_template("index.html", codearea=code )


@app.route("/get_code", methods=['POST'])
def pull_code_snippet():
    if request.method == 'POST':

        code = Info.revertSuccesfulCode
        return render_template('index.html', codearea=code,)
    else:
        return render_template('index.html')




app.run(debug=True)