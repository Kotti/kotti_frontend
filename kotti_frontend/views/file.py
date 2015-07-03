from kotti.resources import File
from kotti.views.file import attachment_view


def includeme(config):
    config.add_view(attachment_view,
                    context=File,
                    permission='pview')
