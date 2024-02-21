from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello web service Credit Financial Holdings'

if __name__ == '__main__':
    app.run()
