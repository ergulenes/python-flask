from cgitb import html
from email.quoprimime import body_check
from pydoc import HTMLDoc
from unicodedata import name
from unittest import result
from flask import Flask, render_template, redirect, url_for, request

app = Flask (__name__)


#learned login page
@app.route("/login", methods=['POST','GET'])
def Login():
    if request.method == 'POST':
        username=request.form["username"]#in login.html created form 
        return redirect(url_for("HelloUser", name=username)) #moved username to hellouser as name
    return render_template("login.html") 




@app.route("/hello-user/<name>")
def HelloUser(name):
    registered_user = ["enes","yakup","melek"] #created regşstered users
    for i in registered_user : 
        return redirect(url_for("Hello", name=name)) #if users is registered it will go hello function
    return render_template("hello_user.html", name=name)





@app.route("/hello/<name>")
def Hello(name):
    return render_template("hello.html", abc=name)




#learned calculation with numbers but there is not interface but learned interface with login.html
@app.route("/add/<number1>/<number2>")
def Calculation(number1, number2):
    calculation_result = int(number1) + int(number2)
    return render_template("add.html", number1=number1, number2=number2, res=calculation_result)

