from flask import Flask

app = Flask(__name__)

words_set = []


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
