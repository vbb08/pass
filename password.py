from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pass/', methods=['GET'])
def show_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    signs = ['#', '@', '!', '$', '&', '%']

    random_letters = random.sample(letters, 5)
    random_upper_letters = random.sample(letters, 2)
    random_upper_letters = [x.upper() for x in random_upper_letters]
    random_numbers = random.sample(numbers, 1)
    random_signs = random.sample(signs, 1)
    z = random_letters + random_upper_letters + random_numbers + random_signs

    random.shuffle(z)

    password = ''
    password = password.join(z)

    show_password = password

    return render_template('index.html', show_password = show_password)

if __name__ == "__main__":
    app.run(debug=True)
