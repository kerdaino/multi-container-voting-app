from flask import Flask, render_template
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "voting_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


@app.route("/")
def results():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT option_name, COUNT(*) 
        FROM votes 
        GROUP BY option_name
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    results_data = {
        "Docker": 0,
        "Kubernetes": 0
    }

    for option_name, count in rows:
        results_data[option_name] = count

    return render_template("results.html", results=results_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)