from pyramid.view import notfound_view_config


@notfound_view_config(
    renderer='kotti_frontend:templates/notfound.pt',
    )
def notfound_view(request):
    request.response.status = '404 Not Found'
    return {}


def includeme(config):  # pragma: no cover
    config.scan(__name__)
