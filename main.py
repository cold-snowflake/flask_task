from flask import Flask, request

from utils import generate_password, generate_name, count_astros 


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


@app.route('/requirements')
def upload_and_run():
    with open('requirements.txt', encoding='Latin1') as file:
        return file.read()


@app.route("/generate-users")
def users():
    length = request.args.get('length', '100')
    if length.isdigit():
        length = int(length)
        if length > 100:
            return "Length should be less than 100"
    else:
        return f"Invalid input value {length}"
    return generate_name(length)


@app.route("/space")
def count():
    return count_astros()



if __name__ == "__main__":
    app.run()