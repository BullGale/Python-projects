from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/guess/<name>')
def guess(name):
    response1 = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = response1.json()
    gender = gender_data["gender"]
    response2 = requests.get(f"https://api.agify.io?name={name}")
    age_data = response2.json()
    age = age_data["age"]
    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route('/')
def blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template('index.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

# Console: document.body.contentEditable=true