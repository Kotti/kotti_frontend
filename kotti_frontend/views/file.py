from pyramid.view import view_config

from kotti.resources import File
from kotti.views.file import attachment_view


@view_config(context=File, permission='pview')
def file_view(request):
    return attachment_view(request.context, request)
