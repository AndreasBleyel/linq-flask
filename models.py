from app import db

class Result(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    wt1 = db.Column(db.String())
    wt2 = db.Column(db.String())
    wt3 = db.Column(db.String())

    def __init__(self, wt1, wt2, wt3):
        self.wt1 = wt1
        self.wt2 = wt2
        self.wt3 = wt3

    def __repr__(self):
        return '<id {}>'.format(self.id)