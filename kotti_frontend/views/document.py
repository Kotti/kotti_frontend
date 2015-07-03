from pyramid.view import view_config
from kotti.resources import Document


@view_config(context=Document,
             renderer='kotti_frontend:templates/mytemplate.pt',
             name='view',
             permission='pview')
def document_view(request):
    return {'one': request.context, 'project': 'kotti_frontend'}


def includeme(config):
    config.scan(__name__)
