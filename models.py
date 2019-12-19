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

class Cards(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    gameid = db.Column(db.Integer)
    p1 = db.Column(db.String())
    p2 = db.Column(db.String())
    p3 = db.Column(db.String())
    p4 = db.Column(db.String())
    p5 = db.Column(db.String())
    p6 = db.Column(db.String())
    p7 = db.Column(db.String())
    p8 = db.Column(db.String())

    def __init__(self, gameid, p1, p2, p3, p4, p5, p6, p7, p8):
        self.gameid = gameid
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7
        self.p8 = p8


    def __repr__(self):
        return '<id {}>'.format(self.id)