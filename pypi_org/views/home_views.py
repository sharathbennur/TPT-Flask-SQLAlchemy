import flask
from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import package_service


blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='Home/index.html')
def index():
    test_packages = package_service.get_test_packages()
    return {'packages': test_packages}


@blueprint.route('/about')
@response(template_file='Home/about.html')
def about():
    return {}
