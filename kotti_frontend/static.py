from pyramid_html_minifier.config import DEFAULT_PLACEHOLDER

def includeme(config):   # pragma: no cover
    config.add_static_view('static', 'static', cache_max_age=3600)   # TODO: remove me

    settings = config.registry.settings
    placeholder = settings.get('pyramid_html_minifier.placeholder', DEFAULT_PLACEHOLDER)

    # styles
    default_styles_path = 'kotti_frontend:templates/{0}/styles/'.format(DEFAULT_PLACEHOLDER)
    config.add_static_view('styles',
                           default_styles_path)
    if placeholder == DEFAULT_PLACEHOLDER:  # add use_sass option
        config.override_asset(to_override=default_styles_path,
                              override_with='kotti_frontend:templates/.tmp/styles/')
    else:
        styles_path = 'kotti_frontend:templates/{0}/styles/'.format(placeholder)
        config.override_asset(to_override=default_styles_path,
                              override_with=styles_path)

    # bower_components
    if placeholder == DEFAULT_PLACEHOLDER:
        # assume not production
        config.add_static_view('bower_components',
                               'kotti_frontend:templates/bower_components/')

    # scripts
    default_scripts_path = 'kotti_frontend:templates/{0}/scripts/'.format(DEFAULT_PLACEHOLDER)
    config.add_static_view('scripts',
                           default_scripts_path)
    if placeholder != DEFAULT_PLACEHOLDER:
        # assume not production
        scripts_path = 'kotti_frontend:templates/{0}/scripts/'.format(placeholder)
        config.override_asset(to_override=default_scripts_path,
                              override_with=scripts_path)

    # fonts
    default_fonts_path = 'kotti_frontend:templates/{0}/fonts/'.format(DEFAULT_PLACEHOLDER)
    config.add_static_view('fonts',
                           default_fonts_path)
    if placeholder == DEFAULT_PLACEHOLDER:
        config.override_asset(to_override=default_fonts_path,
                              override_with='kotti_frontend:templates/.tmp/fonts/')
    else:
        fonts_path = 'kotti_frontend:templates/{0}/fonts/'.format(placeholder)
        config.override_asset(to_override=default_fonts_path,
                              override_with=fonts_path)
