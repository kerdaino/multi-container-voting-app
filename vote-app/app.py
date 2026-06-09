from flask import Flask, render_template, request, redirect
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
def index():
    return render_template("index.html")


@app.route("/vote", methods=["POST"])
def vote():
    selected_option = request.form.get("option")

    if selected_option:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO votes (option_name) VALUES (%s)",
            (selected_option,)
        )
        conn.commit()
        cur.close()
        conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)