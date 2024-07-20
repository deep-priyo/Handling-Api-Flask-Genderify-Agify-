from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return "Head to /yourname "


@app.route('/<name>')
def home(name):
    url = f'https://api.genderize.io/?name={name}'
    age=f'https://api.agify.io/?name={name}'
    response = requests.get(url)
    json_data = response.json()
    print(json_data.get('gender'))
    responseAge = requests.get(age)
    json_dataAge = responseAge.json()
    print(json_dataAge.get('age'))

    return render_template("index.html",name=name,age=json_dataAge.get('age'),gender=json_data.get('gender'))

if __name__ == '__main__':
    app.run(debug=True)
