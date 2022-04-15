from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

name="Iman Williamson"
role="UI/UX Designer"
phone="+1-773-870-0264"
email="imansw08@gmail.com"
location="Tampa, FL, USA"


@app.route("/")
def index():
    return render_template("index.html", 
    name=name,
    role=role,
    phone=phone,
    email=email
    )

if __name__ == "__main__":
    app.run(debug=True)