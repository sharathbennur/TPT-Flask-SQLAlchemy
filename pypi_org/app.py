import flask

app = flask.Flask('pypi')


def get_test_packages():
    return [
        {'name': 'flask', 'version': '1.1.3'},
        {'name': 'sqlalchemy', 'version': '2.2.0'},
        {'name': 'passlib', 'version': '1.0.0'},
    ]


@app.route('/')
def index():
    test_packages = get_test_packages()
    return flask.render_template('Home/index.html', packages=test_packages)

@app.route('/about')
def about():
    return flask.render_template('Home/about.html')


if __name__ == '__main__':
    app.run(debug=True)
