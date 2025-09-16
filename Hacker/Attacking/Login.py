from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Simple user database (insecure)

# HTML template
login_page = """
<!doctype html>
<html>
<head>
    <title>Vulnerable Login</title>
</head>
<body>
    <h2>Login Page (Insecure)</h2>
    <form method="POST">
        Username: <input type="text" name="username" /><br>
        Password: <input type="password" name="password" /><br>
        <input type="submit" value="Login" />
    </form>
    {% if error %}
        <p style="color:red">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Vulnerable check: no hashing, plain comparison
        if username in users and users[username] == password:
            return f"<h2>Welcome {username}!</h2>"
        else:
            error = "Invalid credentials!"
    return render_template_string(login_page, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
