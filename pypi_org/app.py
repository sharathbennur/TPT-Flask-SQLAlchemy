import flask

app = flask.Flask('pypi')

@app.route('/')
def index():
    return "Hello, World"

app.run()
