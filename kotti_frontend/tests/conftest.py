from pytest import fixture

pytest_plugins = "kotti"


@fixture(scope='session')
def custom_settings():
    return {
        'kotti.use_workflow': 'kotti_frontend:workflows/simple_frontend.zcml',
        }
