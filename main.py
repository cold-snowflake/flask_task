from flask import Flask, request
import sqlite3

from utils import generate_password, generate_name, count_astros,commit_sql


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


@app.route('/phones/create')
def phones_create():
    contact_name = request.args['contact-name']
    phone_value = request.args['phone-value']

    sql = f"""
    INSERT INTO Phones (contactName, phoneValue)
    VALUES ('{contact_name}', '{phone_value}');
    """
    
    commit_sql(sql)

    return 'phones_create'


@app.route('/phones/read')
def phones_read():
    con = sqlite3.connect("example.db")
    cur = con.cursor()

    sql = """
    SELECT * FROM Phones;
    """

    cur.execute(sql)
    result = cur.fetchall()
    con.close()
    return str(result)

@app.route('/phones/update')
def phones_update():
    contact_name = request.args['contact-name']
    phone_value = request.args['phone-value']
    phone_id = request.args['phone_id']


    sql = f"""
    UPDATE Phones 
    SET  phoneValue = '{phone_value}',
    contactName = '{contact_name}'
    WHERE  phoneID = {phone_id};
    """
    
    commit_sql(sql)

    return 'phones_update'

@app.route('/phones/delete')
def phones_delete():
    phone_id = request.args['phone_id']


    sql = f"""
    DELETE FROM Phones 
    WHERE  phoneID = {phone_id};
    """

    commit_sql(sql)

    return 'phones_delete'

if __name__ == "__main__":
    app.run()