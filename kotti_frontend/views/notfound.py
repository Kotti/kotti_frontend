from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config


@view_config(context=HTTPNotFound,
             renderer='kotti_frontend:templates/notfound.pt',
             )
def notfound_view(request):
    return {'one': request.context, 'project': 'kotti_frontend'}


def includeme(config):
    config.scan(__name__)
