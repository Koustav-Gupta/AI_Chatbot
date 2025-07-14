from flask import Flask, render_template, request
from chatbot.model import get_response
import sqlite3
from datetime import datetime

app = Flask(__name__)

def log_interaction(user_input, bot_response):
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS chat_log
                      (timestamp TEXT, user_input TEXT, bot_response TEXT)''')
    cursor.execute("INSERT INTO chat_log VALUES (?, ?, ?)",
                   (datetime.now(), user_input, bot_response))
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        response = get_response(user_input)
        log_interaction(user_input, response)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)