from pyramid.view import view_config
from pyramid.renderers import get_renderer


@view_config(route_name='home', renderer='templates/index.pt')
def my_view(request):
    master = get_renderer('templates/master.pt').implementation()
    return {'project': 'free4sale','master':master}
