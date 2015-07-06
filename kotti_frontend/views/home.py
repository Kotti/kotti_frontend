from pyramid.view import view_config

from kotti import DBSession
from kotti.resources import Document


@view_config(context=Document,
             root_only=True,
             renderer='kotti_frontend:templates/mytemplate.pt')
def home_view(request):
    # you can register a different home page view
    return {'project': 'kotti_frontend'}


def includeme(config):
    config.scan(__name__)
