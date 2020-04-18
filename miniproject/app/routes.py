from app import app
from flask import render_template,request,url_for,redirect
from bs4 import BeautifulSoup
import requests


@app.route('/', methods=['GET'])
def index():
    return render_template("/index.html")

@app.route("/essay",methods=["POST"])
def essay():
    input_form = request.form
    k1 = input_form.get("k1")
    k2 = input_form.get("k2")
    k3 = input_form.get("k3")
    print(k1, k2, k3)
    data = requests.get("http://babel-generator.herokuapp.com/?keyword="+k1+"&keyword="+k2+"&keyword="+k3+"&generate=").text
    soup = BeautifulSoup(data)
    essay_content = ""
    for para in soup.find('div', {'class':"essay-contents"}).findAll('p'):
        essay_content += para.contents[0]
    print(essay_content)
    return render_template("essay.html",data={"essay_content":essay_content,"k1":k1, "k2":k2, "k3": k3})