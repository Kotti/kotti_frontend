from pyramid.httpexceptions import HTTPForbidden
from pyramid.view import view_config


@view_config(context=HTTPForbidden,
             renderer='kotti_frontend:templates/forbidden.pt',
             )
def forbidden_view(request):
    return {'one': request.context, 'project': 'kotti_frontend'}


def includeme(config):
    config.scan(__name__)
