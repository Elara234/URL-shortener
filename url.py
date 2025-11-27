from flask import Flask, request, redirect, render_template_string
import random, string

app = Flask(__name__)
urls = {}

@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="POST":
        long_url = request.form["longurl"]
        short = ''.join(random.choices(string.ascii_letters+string.digits, k=5))
        urls[short] = long_url
        return f"Short URL: <a href='/{short}'>/{short}</a>"
    return '''<form method="post">URL: <input name="longurl"><input type="submit"></form>'''

@app.route("/<short>")
def redirect_short(short):
    return redirect(urls.get(short, "/"))

if __name__=="__main__":
    app.run(debug=True)
