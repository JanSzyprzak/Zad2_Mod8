from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route("/mypage/me")
def about_me():
    return render_template("about_me.html")

@app.route("/mypage/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print(request.form['text'])
        return redirect("/mypage/me")
    elif request.method == 'GET':
        return render_template("contact.html")