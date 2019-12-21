import os
from app import app, db

app.config.from_object(os.environ['APP_SETTINGS'])

def reset_db():
    db.session.execute('''TRUNCATE TABLE games''')
    db.session.execute('''TRUNCATE TABLE cards''')
    db.session.execute('''ALTER SEQUENCE games_id_seq RESTART WITH 1''')
    db.session.execute('''ALTER SEQUENCE cards_id_seq RESTART WITH 1''')
    db.session.commit()

reset_db()