import copy
from sqlalchemy import engine_from_config
from sqlalchemy.exc import UnboundExecutionError
from pyramid.config import Configurator
from kotti import (
    conf_defaults as kotti_conf_defaults,
    DBSession,
    _resolve_dotted,
    )
from kotti.resources import initialize_sql

frontend_includes = [
    'kotti',
    'kotti.views',   # custom kotti predicates
    ]

conf_defaults = copy.deepcopy(kotti_conf_defaults)
conf_defaults['kotti.base_includes'] = ' '.join(frontend_includes)


def main(global_config, **settings):
    # This function is a 'paste.app_factory' and returns a WSGI
    # application.

    config = base_configure(global_config, **settings)
    try:
        DBSession.get_bind()
    except UnboundExecutionError:
        # are you are running frontend-dev.ini standalone?
        engine = engine_from_config(config.registry.settings, 'sqlalchemy.')
        initialize_sql(engine)

    return config.make_wsgi_app()


def base_configure(global_config, **settings):
    # Resolve dotted names in settings, include plug-ins and create a
    # Configurator.

    from kotti.resources import get_root

    for key, value in conf_defaults.items():
        settings.setdefault(key, value)

    for key, value in settings.items():
        if key.startswith('kotti') and isinstance(value, basestring):
            settings[key] = unicode(value, 'utf8')

    # Allow extending packages to change 'settings' w/ Python:
    k = 'kotti.configurators'
    for func in _resolve_dotted(settings, keys=(k,))[k]:
        func(settings)

    settings = _resolve_dotted(settings)
    secret1 = settings['kotti.secret']
    settings.setdefault('kotti.secret2', secret1)

    # We'll process ``pyramid_includes`` later by hand, to allow
    # overrides of configuration from ``kotti.base_includes``:
    pyramid_includes = settings.pop('pyramid.includes', '')

    config = Configurator(
        request_factory=settings['kotti.request_factory'][0],
        settings=settings)
    config.begin()

    config.hook_zca()
    config.include('pyramid_zcml')

    # Chameleon bindings were removed from Pyramid core since pyramid>=1.5a2
    config.include('pyramid_chameleon')

    config.registry.settings['pyramid.includes'] = pyramid_includes

    # Include modules listed in 'kotti.base_includes':
    for module in settings['kotti.base_includes']:
        config.include(module)
    config.commit()

    # Modules in 'pyramid.includes' and 'kotti.zcml_includes' may
    # override 'kotti.base_includes':
    if pyramid_includes:
        for module in pyramid_includes.split():
            config.include(module)

    for name in settings['kotti.zcml_includes'].strip().split():
        config.load_zcml(name)

    config.commit()

    config._set_root_factory(get_root)

    return config
