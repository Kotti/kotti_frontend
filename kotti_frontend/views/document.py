from pyramid.view import view_config
from kotti.resources import Document


@view_config(context=Document,
             renderer='kotti_frontend:templates/{0}/index.html',
             name='view',
             permission='pview')
def document_view(request):
    return {}


def includeme(config):   # pragma: no cover
    config.scan(__name__)
