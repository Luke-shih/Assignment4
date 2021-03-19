from flask import Flask, request, render_template, session, url_for, redirect

app=Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "assignmentweek4"

@app.route("/")
def homepage():
    return render_template("homepage.html") 

@app.route("/signin", methods=["POST"])
def signin():
    session["account"] = "test"
    session["password"] = "test"
    if request.form["account"] == session["account"] and request.form["password"] == session["password"]:
        return redirect(url_for("member"))
    else:
        return  redirect(url_for("error"))

@app.route("/logout")
def logout():
    session.pop("account", None)
    session.pop("password", None)
    return redirect(url_for("homepage"))

@app.route("/member")
def member():
    return render_template("member.html")

@app.route("/error")
def error():
    return render_template("error.html")

app.run(port=3000) 
