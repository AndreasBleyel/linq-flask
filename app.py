import os, random, logging
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

print('ENV: ' + os.environ['APP_SETTINGS'])

from models import Result, Game, Cards


def create_words(gameid):
    words = []
    nr_rows = db.session.query(Result).count()
    print(nr_rows)

    nr_players = db.session.query(Game.nrplayer).filter_by(id=gameid).first()[0]
    print(nr_players)
    print(type(nr_players))

    id_word1 = random.randint(0, nr_rows - 1)

    id_word2 = random.randint(0, nr_rows - 1)
    while id_word2 == id_word1:
        id_word2 = random.randint(0, nr_rows - 1)

    words.append(db.session.query(Result.word).filter_by(id=id_word1).first())
    words.append(db.session.query(Result.word).filter_by(id=id_word2).first())

    if nr_players == 4:
        print("4 Spieler")
        words.extend(words)
        random.shuffle(words)
        words.extend(["Nur 4 Spieler", "Nur 4 Spieler", "Nur 4 Spieler", "Nur 4 Spieler"])
    elif nr_players == 5:
        words.extend(words)
        words.append("Du bist der Freigeist")
        random.shuffle(words)
        words.extend(["Nur 5 Spieler", "Nur 5 Spieler", "Nur 5 Spieler"])
    elif nr_players == 6:
        words.extend(words)
        words.append("Du bist der Freigeist")
        words.append("Du bist der Freigeist")
        random.shuffle(words)
        words.extend(["Nur 6 Spieler", "Nur 6 Spieler"])
    elif nr_players > 6:
        id_word3 = random.randint(0, nr_rows - 1)
        while id_word3 == id_word2:
            id_word3 = random.randint(0, nr_rows - 1)

        words.append(db.session.query(Result.word).filter_by(id=id_word3).first())

        if nr_players == 7:
            words.extend(words)
            words.append("Du bist der Freigeist")
            random.shuffle(words)
            words.append("Nur 7 Spieler")
        elif nr_players == 8:
            words.extend(words)
            words.append("Du bist der Freigeist")
            words.append("Du bist der Freigeist")
            random.shuffle(words)

    for word in words:
        print(word)

    if db.session.query(Cards.id).filter_by(gameid=gameid).first():
        print("Game exists")
        db.session.query(Cards).filter_by(gameid=gameid).update({'p1': words[0],
                                                                 'p2': words[1],
                                                                 'p3': words[2],
                                                                 'p4': words[3],
                                                                 'p5': words[4],
                                                                 'p6': words[5],
                                                                 'p7': words[6],
                                                                 'p8': words[7]})
    else:
        print("New Cards")
        cards = Cards(
            gameid=gameid,
            p1=words[0],
            p2=words[1],
            p3=words[2],
            p4=words[3],
            p5=words[4],
            p6=words[5],
            p7=words[6],
            p8=words[7]
        )
        db.session.add(cards)

    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []

    if request.method == 'POST':
        try:
            number_players = request.form['nr-players']
            game = Game(
                nrplayer=number_players,
                nrround=1
            )
            db.session.add(game)
            db.session.commit()
            print(game.id)

            create_words(game.id)
            return render_template("shuffle.html", round=1, gameid=game.id)
        except:
            errors.append(
                "Falsche Spieleranzahl. Mögliche Anzahl sind 4-8 Spieler"
            )

    return render_template('index.html')


@app.route('/s', methods=['GET', 'POST'])
def shuffle():
    errors = []

    if request.method == 'POST':
        try:
            gameid = int(request.form['shuffle'])
            print("s gid: " + str(gameid))
            print(type(gameid))
            create_words(gameid)
            db.session.query(Game.nrround).filter_by(id=gameid).update({'nrround': Game.nrround + 1})
            db.session.commit()
            nrround = db.session.query(Game.nrround).filter_by(id=gameid).first()[0]
            return render_template("shuffle.html", round=nrround, gameid=gameid)
        except:
            errors.append(
                "Something went wrong /shuffle"
            )

    return render_template("shuffle.html", round='-')


@app.route('/d')
def debug():
    games = db.session.query(Game).all()
    cards = db.session.query(Cards).all()
    words = db.session.query(Result).all()
    return render_template("debug.html", games=games, cards=cards, words=words)


@app.route('/1', methods=['GET', 'POST'])
def send_word_p1():
    errors = []

    if request.method == 'POST':
        try:
            game_id = request.form['gameid']
            word = db.session.query(Cards.p1).filter_by(gameid=game_id).first()[0]

            return render_template("word.html", word=word, plid=1, gameid=game_id)
        except:
            errors.append(
                "Falsche Spieleranzahl. Mögliche Anzahl sind 4-8 Spieler"
            )

    return render_template("word.html", word='Noch kein Wort', plid=1)


@app.route('/2', methods=['GET', 'POST'])
def send_word_p2():
    errors = []

    if request.method == 'POST':
        try:
            game_id = request.form['gameid']
            word = db.session.query(Cards.p2).filter_by(gameid=game_id).first()[0]

            return render_template("word.html", word=word, plid=2, gameid=game_id)
        except:
            errors.append(
                "Falsche Spieleranzahl. Mögliche Anzahl sind 4-8 Spieler"
            )

    return render_template("word.html", word='Noch kein Wort', plid=2)


@app.route('/3', methods=['GET', 'POST'])
def send_word_p3():
    errors = []

    if request.method == 'POST':
        try:
            game_id = request.form['gameid']
            word = db.session.query(Cards.p3).filter_by(gameid=game_id).first()[0]

            return render_template("word.html", word=word, plid=3, gameid=game_id)
        except:
            errors.append(
                "Falsche Spieleranzahl. Mögliche Anzahl sind 4-8 Spieler"
            )

    return render_template("word.html", word='Noch kein Wort', plid=3)


@app.route('/4', methods=['GET', 'POST'])
def send_word_p4():
    errors = []

    if request.method == 'POST':
        try:
            game_id = request.form['gameid']
            word = db.session.query(Cards.p4).filter_by(gameid=game_id).first()[0]

            return render_template("word.html", word=word, plid=4, gameid=game_id)
        except:
            errors.append(
                "Falsche Spieleranzahl. Mögliche Anzahl sind 4-8 Spieler"
            )

    return render_template("word.html", word='Noch kein Wort', plid=4)


@app.route('/5', methods=['GET', 'POST'])
def send_word_p5():
    errors = []

    if request.method == 'POST':
        try:
            game_id = request.form['gameid']
            word = db.session.query(Cards.p5).filter_by(gameid=game_id).first()[0]

            return render_template("word.html", word=word, plid=5, gameid=game_id)
        except:
            errors.append(
                "Falsche Spieleranzahl. Mögliche Anzahl sind 4-8 Spieler"
            )

    return render_template("word.html", word='Noch kein Wort', plid=5)


@app.route('/6', methods=['GET', 'POST'])
def send_word_p6():
    errors = []

    if request.method == 'POST':
        try:
            game_id = request.form['gameid']
            word = db.session.query(Cards.p6).filter_by(gameid=game_id).first()[0]

            return render_template("word.html", word=word, plid=6, gameid=game_id)
        except:
            errors.append(
                "Falsche Spieleranzahl. Mögliche Anzahl sind 4-8 Spieler"
            )

    return render_template("word.html", word='Noch kein Wort', plid=6)


@app.route('/7', methods=['GET', 'POST'])
def send_word_p7():
    errors = []

    if request.method == 'POST':
        try:
            game_id = request.form['gameid']
            word = db.session.query(Cards.p7).filter_by(gameid=game_id).first()[0]

            return render_template("word.html", word=word, plid=7, gameid=game_id)
        except:
            errors.append(
                "Falsche Spieleranzahl. Mögliche Anzahl sind 4-8 Spieler"
            )

    return render_template("word.html", word='Noch kein Wort', plid=7)


@app.route('/8', methods=['GET', 'POST'])
def send_word_p8():
    errors = []

    if request.method == 'POST':
        try:
            game_id = request.form['gameid']
            word = db.session.query(Cards.p8).filter_by(gameid=game_id).first()[0]

            return render_template("word.html", word=word, plid=8, gameid=game_id)
        except:
            errors.append(
                "Falsche Spieleranzahl. Mögliche Anzahl sind 4-8 Spieler"
            )

    return render_template("word.html", word='Noch kein Wort', plid=8)


if __name__ == '__main__':
    app.run()
