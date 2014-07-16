from pyramid.view import view_config
from pyramid.renderers import get_renderer


@view_config(route_name='home', renderer='templates/index.pt')
def index(request):
    master = get_renderer('templates/master.pt').implementation()
    return {'project': 'free4sale','master':master}

@view_config(name='register', renderer='templates/register.pt')
def register(request):
    master = get_renderer('templates/master.pt').implementation()
    return {'project': 'free4sale','master':master}

@view_config(name='add_product', renderer='templates/add_product.pt')
def add_product(request):
    master = get_renderer('templates/master.pt').implementation()
    return {'project': 'free4sale','master':master}
