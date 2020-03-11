import flask
from pypi_org.infrastructure.view_modifiers import response
app = flask.Flask('pypi')


def get_test_packages():
    return [
        {'name': 'flask', 'version': '1.1.3'},
        {'name': 'sqlalchemy', 'version': '2.2.0'},
        {'name': 'passlib', 'version': '1.0.0'},
    ]


@app.route('/')
@response(template_file='Home/index.html')
def index():
    test_packages = get_test_packages()
    return {'packages' : test_packages}


@app.route('/about')
@response(template_file='Home/about.html')
def about():
    return {}


if __name__ == '__main__':
    app.run(debug=True)
