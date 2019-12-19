import os, random
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result

print('ENV: ' + os.environ['APP_SETTINGS'])

def file_to_db():
    filename = 'words'


    print('Words loaded from: ' + filename)


def create_words():
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []

    if request.method == 'POST':
        try:
            number_players = request.form['nr-players']
            return render_template("shuffle.html", round=1)
        except:
            errors.append(
                "Falsche Spieleranzahl. Mögliche Anzahl sind 4-8 Spieler"
            )

    return render_template('index.html')


@app.route('/s')
def shuffle():
    create_words()
    return render_template("shuffle.html", round='not yet')


@app.route('/d')
def debug():
    return render_template("debug.html", words='not yet')


if __name__ == '__main__':
    app.run()
