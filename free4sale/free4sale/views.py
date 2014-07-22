from pyramid.view import view_config
from pyramid.renderers import get_renderer
from pyramid.httpexceptions import HTTPFound
from models import Product
from .models import (DBSession, Product, Person)


@view_config(route_name='home', renderer='templates/index.pt')
def index(request):
    master = get_renderer('templates/master.pt').implementation()
    persons = DBSession.query(Person).all()
    products = DBSession.query(Product).all()
    return {'project': 'free4sale','master':master, 'persons': persons, 'products':products }

@view_config(name='register', renderer='templates/register.pt')
def register(request):
    master = get_renderer('templates/master.pt').implementation()
    return {'project': 'free4sale','master':master}

@view_config(name='add_product', renderer='templates/add_product.pt')
def add_product(request):
    master = get_renderer('templates/master.pt').implementation()
    return {'project': 'free4sale','master':master}

@view_config(name='add_product_save', renderer='templates/add_product_save.pt')
def add_product_save(request):
    fields = request.POST
    name = fields['name']
    pictures = fields['pics']
    description = fields['description']
    price = fields['price']
    condition = fields['condition']
    person = Person(fname="Joao",lname="da Silva")
    product = Product(name=name, picture=pictures, description=description,condition=condition,price=price)
    person.products.append(product)
    DBSession.add(person)
    return HTTPFound(location='/add_product')

@view_config(name='register_save', renderer='templates/add_product_save.pt')
def register_save(request):
    fields = request.POST
    fname = fields['fname']
    lname = fields['lname']
    address = fields['address']
    email = fields['email']
    password = fields['password']
    oncampus = fields['oncampus']
    person = Person(fname=fname,lname=lname,email=email,password=password,oncampus=oncampus)
    DBSession.add(person)
    return HTTPFound(location='/add_product')


