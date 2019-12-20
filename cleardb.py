import os
from app import app, db

app.config.from_object(os.environ['APP_SETTINGS'])

def reset_db():
    db.session.execute('''TRUNCATE TABLE games''')
    db.session.execute('''TRUNCATE TABLE cards''')

reset_db()