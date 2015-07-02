from pyramid.view import view_config

from kotti import DBSession
from kotti.resources import Document


@view_config(route_name='home',
             renderer='kotti_frontend:templates/mytemplate.pt')
def home_view(request):
    one = DBSession.query(Document).first()
    return {'one': one, 'project': 'kotti_frontend'}


def includeme(config):
    config.scan(__name__)
