import factory
from factory import alchemy, Sequence, RelatedFactory
from flask import Flask,url_for
from . import app,db,auth
from ..auth.models import User
from ..blog_mod.blog_factories import BlogFactory


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    name = Sequence(lambda n: 'user{0}'.format(n))
    username = factory.fuzzy.FuzzyText('shrutih')
    email = Sequence(lambda n: 'user{0}@example.com'.format(n))
    password = factory.fuzzy.FuzzyText('sh12345')
    address = factory.fuzzy.FuzzyText('Pune')
    contact = factory.fuzzy.FuzzyInteger(8464876748)
    gender = factory.fuzzy.FuzzyText('Female')
    blogs = factory.SubFactory(BlogFactory)
