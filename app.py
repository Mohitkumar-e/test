from flask import Flask, render_template, request
import random
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    gender = request.form['gender']
    crush = request.form['crush']

    # --- Save user data ---
    with open('love_data.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, gender, crush])

    # --- Random love prediction ---
    outcomes = [
        f"🔥 {name} and {crush} are destined to be soulmates!",
        f"💔 Sorry {name}, {crush} will break your heart.",
        f"💘 Wedding bells are in your future, {name}!",
        f"😅 {crush} will text you... in your dreams.",
        f"🌹 It’s complicated, {name}. Very complicated.",
        f"😂 You’ll be besties forever — just not lovers."
    ]

    result = random.choice(outcomes)

    return f"""
    <h1 style='text-align:center; color:hotpink;'>{result}</h1>
    <div style='text-align:center; margin-top:20px;'>
        <a href='/'>Try Again 💫</a>
    </div>
    <div style='text-align:center; margin-top:30px;'>
        <video width="480" autoplay controls>
            <source src="/static/lovevideo.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True)
