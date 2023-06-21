import sqlite3


def create_table():
    con = sqlite3.connect("example.db")
    cur = con.cursor()

    sql = '''
    CREATE TABLE Phones (
    phoneID INTEGER PRIMARY KEY,
    contactName varchar(255), 
    phoneValue varchar(255)
    )
    '''

    cur.execute(sql)
    con.commit()
    con.close()

if __name__ == '__main__':
    create_table()
