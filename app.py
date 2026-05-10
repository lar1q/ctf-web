from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)

DB_NAME = "ctf.db"

def init_db():

    if os.path.exists(DB_NAME):
        return

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
    ''')

    cur.execute("""
    INSERT INTO users(username,password)
    VALUES('admin','1234')
    """)

    cur.execute('''
    CREATE TABLE q_71337(
        id INTEGER PRIMARY KEY,
        noise TEXT
    )
    ''')

    rickroll = '''
110100001011001011010001100000011101000010110101001000001101000010111101110100001011000011010000101111001101000010111101110100001011111011010000101100111101000010111110001000001101000110000001110100001011101111010000101111101101000010110110110100001011110111010000101101011101000010110101
'''

    cur.execute(
        'INSERT INTO q_71337(noise) VALUES(?)',
        (rickroll,)
    )

    cur.execute('''
    CREATE TABLE internal_archive_9437(
        id INTEGER PRIMARY KEY,
        fragment TEXT
    )
    ''')

    real_code = r'''
s = ""
i = 1

while True:

    if i % 2 != 0:
        s += "0"
    else:
        s += "1"

    if i % 3 != 0:
        s += "1"
    else:
        s += "0"

    if i % 5 != 0:
        s += "1"
    else:
        s += "0"

    # ????

    if i % 11 != 0:
        s += "0"
    else:
        s += "1"

    if i % 13 != 0:
        s += "1"
    else:
        s += "0"

    if i % 17 != 0:
        s += "0"
    else:
        s += "1"

    if i % 19 != 0:
        s += "1"
    else:
        s += "0"

    i += 1

    if len(s) >= 240:
        break

print(s)
'''

    cur.execute(
        'INSERT INTO internal_archive_9437(fragment) VALUES(?)',
        (real_code,)
    )

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():

    user = request.args.get('user', '')

    lowered = user.lower()

    if "union select fragment from internal_archive_9437--" in lowered:
        return "blocked"

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    query = f"""
    SELECT username
    FROM users
    WHERE username = '{user}'
    """

    try:

        result = cur.execute(query).fetchall()

        return str(result)

    except Exception as e:

        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
