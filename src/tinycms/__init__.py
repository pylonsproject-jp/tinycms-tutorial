from pyramid.config import Configurator
from pyramid_zodbconn import get_connection
from pyramid.events import subscriber
from .models import appmaker


def includeme(config):
    config.scan(".")

class MemoryTmpStore(dict):
    def preview_url(self, name):
        return None

memory_tmp_store = MemoryTmpStore()

def root_factory(request):
    conn = get_connection(request)
    return appmaker(conn.root())


@subscriber('pyramid.events.BeforeRender')
def register_globals(event):
    from . import helpers
    event['h'] = helpers

def main(global_conf, **settings):
    config = Configurator(settings=settings,
                          root_factory=root_factory)
    config.include('pyramid_tm')
    config.include('pyramid_zodbconn')
    config.include('pyramid_deform')
    config.include('pyramid_layout')
    config.include('deform_bootstrap')
    config.include(".")
    return config.make_wsgi_app()
