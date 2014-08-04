from pyramid.view import view_config
from pyramid.renderers import get_renderer
from pyramid.httpexceptions import HTTPFound
from models import Product
from .models import (DBSession, Product, User)
from urllib import urlencode
from pyramid.view import (
    view_config,
    forbidden_view_config,
    )

from pyramid.security import (
    remember,
    forget,
    )

def generateFromMaster(page_params = {}):
    page_params['categories'] = ['Art','Books','Fashion','Furniture','Electrics','Products','Vehicle']
    page_params['master'] = get_renderer('templates/master.pt').implementation()
    page_params['project'] = 'free4sale'
    return page_params

def url_message_generator(msg_type, message):
    types = ["danger", "warning", "success"]
    if msg_type in types:
        return urlencode({"msg_show":True,"msg_text":message,'msg_type':msg_type})
    else:
        raise Exception("type message not exist")

@view_config(route_name='home', renderer='templates/index.pt')
def index(request):
    master = get_renderer('templates/master.pt').implementation()
    users = DBSession.query(User).all()
    products = DBSession.query(Product).all()
    return generateFromMaster({'users': users, 'products':products })

@view_config(name='register', renderer='templates/register.pt')
def register(request):
    master = get_renderer('templates/master.pt').implementation()
    return generateFromMaster()

@view_config(name='add_product', renderer='templates/add_product.pt')
def add_product(request):
    master = get_renderer('templates/master.pt').implementation()
    return generateFromMaster()

@view_config(name='add_product_save')
def add_product_save(request):
    fields = request.POST
    name = fields['name']
    pictures = fields['pics']
    description = fields['description']
    price = fields['price']
    condition = fields['condition']
    user = User(fname="Joao",lname="da Silva")
    product = Product(name=name, picture=pictures, description=description,condition=condition,price=price)
    user.products.append(product)
    DBSession.add(user)
    return HTTPFound(location='/add_product')

@view_config(name='register_save')
def register_save(request):
    fields = request.POST
    fname = fields['fname']
    lname = fields['lname']
    address = fields['address']
    email = fields['email']
    password = fields['password']
    oncampus = fields['oncampus']
    user = User(fname=fname,lname=lname,email=email,password=password,oncampus=oncampus)
    DBSession.add(user)
    return HTTPFound(location='/add_product')

def find_query_in_products(products,query):
    result = []
    for p in products:
        if query in p.name:
            result.append(p)
        elif query in p.description:
            result.append(p)
        elif query in p.category:
            result.append(p)
    return products

@view_config(name='search_query',renderer='templates/search_results.pt')
def search_query(request):
    all_products = DBSession.query(Product).all()

    if request.GET.get('search'):
        query = request.GET['search']
        products = find_query_in_products(all_products,query)

    #There is no difference from "search" yet.
    if request.GET.get('category'):
        category = request.GET['category']
        products = find_query_in_products(all_products,category)

    master = get_renderer('templates/master.pt').implementation()
    return generateFromMaster({'products': products})


@view_config(name='login')
def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = DBSession.query(User).filter(User.email == email).first()
    print "#"
    print user.fname
    print "#"
    if user != [] and user.password == password:
        headers = remember(request, email)
        return HTTPFound(location = "/?" + url_message_generator("success","You logged in."),
                             headers = headers)
    else:
        return HTTPFound(location = "/")

@view_config(name='islogged',renderer='json')
def islogged(request):
    logged_in = request.authenticated_userid
    print "Logged_in",logged_in
    return {'logged':logged_in}

@view_config(name='users',renderer='templates/list_users.pt')
def users(request):
    users = DBSession.query(User).all()
    master = get_renderer('templates/master.pt').implementation()
    return generateFromMaster({'users':users})

@view_config(name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = "/", headers = headers)

