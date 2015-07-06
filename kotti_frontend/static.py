def includeme(config):   # pragma: no cover
    config.add_static_view('static', 'static', cache_max_age=3600)
