from flask import Flask, request

from utils import generate_password


app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello_world():
    return"<p>Hello, world!<p>"

@app.route("/password")
def password():
    length = request.args.get('length', 10)

    if length.isdigit():
        length = int(length)
        
        if length > 100:
           return "Length should be less than 100"
    else:
        return f"Invalid input value {length}"
    return generate_password(length)



if __name__ == "__main__":
    app.run()