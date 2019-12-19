from app import db

class Result(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String())

    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    nrplayer = db.Column(db.Integer)
    nrround = db.Column(db.Integer)

    def __init__(self, nrplayer, nrround):
        self.nrplayer = nrplayer
        self.nrround = nrround

    def __repr__(self):
        return '<id {}>'.format(self.id)