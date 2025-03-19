from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://bockslunch_render_db_user:kuiNmHM1X0fiqIkKVgAo3326iRfK8vgH@dpg-cvcus3dds78s7384rmbg-a/bockslunch_render_db")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://bockslunch_render_db_user:kuiNmHM1X0fiqIkKVgAo3326iRfK8vgH@dpg-cvcus3dds78s7384rmbg-a/bockslunch_render_db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First VARCHAR(255),
        Last VARCHAR(255),
        City VARCHAR(255),
        Name VARCHAR(255),
        Number INT
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgresql://bockslunch_render_db_user:kuiNmHM1X0fiqIkKVgAo3326iRfK8vgH@dpg-cvcus3dds78s7384rmbg-a/bockslunch_render_db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES 
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        {'Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgresql://bockslunch_render_db_user:kuiNmHM1X0fiqIkKVgAo3326iRfK8vgH@dpg-cvcus3dds78s7384rmbg-a/bockslunch_render_db")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://bockslunch_render_db_user:kuiNmHM1X0fiqIkKVgAo3326iRfK8vgH@dpg-cvcus3dds78s7384rmbg-a/bockslunch_render_db")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string
