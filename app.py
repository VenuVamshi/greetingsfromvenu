from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def greet():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        message = f"Hi {username}! 🎂 Have a wonderful day! — from Venu 🎉"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)