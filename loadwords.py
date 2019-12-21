import os
from app import app, db
from models import Result

app.config.from_object(os.environ['APP_SETTINGS'])

def file_to_db():

    db.session.execute('''TRUNCATE TABLE words''')
    db.session.execute('''ALTER SEQUENCE words_id_seq RESTART WITH 1''')

    filename = 'words'
    with open(filename, "r") as f:
        for item in f:
            word = item.rstrip('\n')
            result = Result(
                word=word
            )
            db.session.add(result)

        db.session.commit()

    print('Words loaded from: ' + filename)

file_to_db()
