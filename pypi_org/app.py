import flask

app = flask.Flask('pypi')


@app.route('/')
def index():
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
