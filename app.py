from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():

    user = request.args.get('user', '')

    # маленький bait-фильтр
    lowered = user.lower()

    if "union select fragment from internal_archive_9437--" in lowered:
        return "blocked"

    conn = sqlite3.connect('ctf.db')
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
    app.run(debug=True)
