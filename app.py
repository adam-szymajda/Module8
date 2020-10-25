from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/me', methods=['GET'])
def greeting():
    tab = "About me"
    return render_template("aboutme.html", tab=tab)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "GET":
        tab = "Contact"
        data = {'phone':'00487483986', 'email': 'adam.szymajda@gmail.com', 'street':'Ulica Jakaś 48', 'city':'Warszawa', 'district':'Ochota'}
        return render_template("contact.html", items = data, tab=tab)
    if request.method == "POST":
        print(request.form)
        return redirect("/me")
