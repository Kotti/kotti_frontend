from pytest import fixture

pytest_plugins = "kotti"

from kotti_frontend import frontend_includes


@fixture(scope='session')
def custom_settings():
    return {
        'kotti.use_workflow': 'kotti_frontend:workflows/simple_frontend.zcml',
        'pyramid.includes': ' '.join(frontend_includes),
        }
