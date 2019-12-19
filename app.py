import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

words_set = []
print('ENV: ' + os.environ['APP_SETTINGS'])

def read_word_file():
    with open("words", "r") as f:
        for item in f:
            line = item.rstrip('\n')
            words_set.append(line)


@app.route('/')
def hello_world():
    read_word_file()
    return 'Hello ' + str(len(words_set))


if __name__ == '__main__':
    app.run()
