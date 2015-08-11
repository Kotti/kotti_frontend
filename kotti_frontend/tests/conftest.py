from pytest import fixture

pytest_plugins = "kotti"


@fixture(scope='session')
def custom_settings():
    return {
        'kotti.site_title': 'kotti_frontend',
        'kotti.use_workflow': 'kotti_frontend:workflows/simple_frontend.zcml',
        'kotti.base_includes': ' '.join(('kotti', 'kotti.views',))
        }
