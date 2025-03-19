from flask import Flask
from flask import jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Christopher Taylor in 3308'

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
        CREATE TABLE IF NOT EXISTS "Basketball" (
        First VARCHAR(255),
        Last VARCHAR(255),
        City VARCHAR(255),
        Name VARCHAR(255),
        Number INT
        );
        ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def inserting():
    try:
        conn = psycopg2.connect("postgresql://bockslunch_render_db_user:kuiNmHM1X0fiqIkKVgAo3326iRfK8vgH@dpg-cvcus3dds78s7384rmbg-a/bockslunch_render_db")
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO Basketball (First, Last, City, Name, Number)
            VALUES 
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
            ('Christopher', 'Taylor', 'CU Boulder', 'Burndown For What', 3308);
        ''')
        conn.commit()
        cur.close()
        conn.close()
        return "Basketball Table Successfully Populated"
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgresql://bockslunch_render_db_user:kuiNmHM1X0fiqIkKVgAo3326iRfK8vgH@dpg-cvcus3dds78s7384rmbg-a/bockslunch_render_db")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball Table Successfully Dropped"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://bockslunch_render_db_user:kuiNmHM1X0fiqIkKVgAo3326iRfK8vgH@dpg-cvcus3dds78s7384rmbg-a/bockslunch_render_db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball;')
    records = cur.fetchall()
    cur.close()
    conn.close()

    response_string = "<table border='1'><thead><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr></thead><tbody>"
    for player in records:
        response_string += "<tr>" + "".join(f"<td>{info}</td>" for info in player) + "</tr>"
    response_string += "</tbody></table>"
    return response_string

