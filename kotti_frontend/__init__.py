import copy
from pyramid.config import Configurator
from kotti import conf_defaults as kotti_conf_defaults
from kotti import _resolve_dotted

conf_defaults = copy.deepcopy(kotti_conf_defaults)
conf_defaults['kotti.base_includes'] = 'kotti'

frontend_includes = [
    'kotti_frontend.views.image',
    'kotti_frontend.views.file',
    'kotti_frontend.views.home',
    'kotti_frontend.views.document',
    'kotti_frontend.views.notfound',
    'kotti_frontend.views.forbidden',
    ]


def main(global_config, **settings):
    # This function is a 'paste.app_factory' and returns a WSGI
    # application.

    config = base_configure(global_config, **settings)

    ###
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    for include in frontend_includes:
        config.include(include)
    ###
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
