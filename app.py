from flask import Flask, request, render_template, session, url_for, redirect

app=Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "assignmentweek4"

@app.route("/")
def homepage(): # 一進入"/"時先切換到 homepage 首頁
    return render_template("homepage.html") 

@app.route("/signin", methods=["POST"]) # 首頁中, 當輸入完 account 和 password 後按下登入按鈕會執行 /signin
def signin():
    if request.form["account"] == "test" and request.form["password"] == "test": # 先檢查輸入的帳號密碼是不是都是 test
        session["account"] = "test"     # 如果是就把帳號密碼設定 session
        session["password"] = "test"
        return redirect(url_for("member")) # 設定完跳轉到 "/member"
    else:
        return redirect(url_for("error")) # 如果帳號密碼有一個不等於 test 則跳到 "/error"

@app.route("/member")
def member():
    if "account" in session and "password" in session:
        return render_template("member.html")
    else:
        return redirect(url_for("error"))

@app.route("/signout/")   # 設定按下登出後執行
def logout():
    session.pop("account", None)    # 將 account 清空
    session.pop("password", None)   # 將 password 清空
    return redirect(url_for("homepage"))    # 回傳到首頁

@app.route("/error") # 當帳號密碼有一個不等於 test 時執行
def error():
    return render_template("error.html")

app.run(port=3000)
