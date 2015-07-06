from pyramid.view import forbidden_view_config


@forbidden_view_config(
    renderer='kotti_frontend:templates/forbidden.pt',
    )
def forbidden_view(request):
    request.response.status = '403 Forbidden'
    return {}


def includeme(config):  # pragma: no cover
    config.scan(__name__)
