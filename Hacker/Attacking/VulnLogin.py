from flask import Flask,redirect,url_for,render_template,request,session,flash
import mysql.connector

def DataBase():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="abebaws"
    )
app = Flask(__name__)
app.secret_key="Haxking_lab"
pas="1234"
name="root"
@app.route("/login/",methods=["GET","POST"])
def login():
    con = DataBase()
    if con.is_connected():
        print("Connected to MySQL database")
    cur=con.cursor()
    cur.execute("create database if not exists TryH")
    print("Database is created")
    cur.execute("use TryH")
    cur.execute("CREATE TABLE if not exists users (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), pass VARCHAR(255))")
    print("Tabel is created")
    if request.method == "POST":
        username=request.form["username"]
        password=request.form["password"]
        #return f"<script>alert({username:password})</script>"
        #cur.execute(f"SELECT * FROM users WHERE username = '{username}' AND password ='{password}'")
        sql = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
        cur.execute(sql)
        user=cur.fetchone()
        cur.close()
        con.close()
        if user:
            session["user"] = username
            return redirect(url_for("DashBoard"))
        else:
            flash("Invaild value")
    return render_template('VulnLogin.html')
@app.route("/")
def DashBoard():
    if "user" not in session:
        flash("Please login first !!")
        return redirect(url_for("login"))
    return render_template("DashB.html",user=session["user"])

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))
app.run(port=5002)
