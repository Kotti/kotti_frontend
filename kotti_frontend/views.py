from pyramid.view import view_config

from kotti import DBSession
from kotti.resources import Document


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    one = DBSession.query(Document).first()
    return {'one': one, 'project': 'kotti_frontend'}
