from pytest import fixture

pytest_plugins = "kotti"

from kotti_frontend import frontend_includes


@fixture(scope='session')
def custom_settings():
    return {
        'kotti.site_title': 'kotti_frontend',
        'kotti.use_workflow': 'kotti_frontend:workflows/simple_frontend.zcml',
        'kotti.asset_overrides': 'kotti_frontend:templates/app/kotti-overrides/',
        'pyramid.includes': ' '.join(frontend_includes),
        }
