from app import db

class Result(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String())

    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return '<id {}>'.format(self.id)