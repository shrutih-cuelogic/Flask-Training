import factory
from factory import alchemy, Sequence, RelatedFactory
from flask import Flask,url_for
from . import app,db,auth
from ..auth.models import User
from ..auth.auth_factories import UserFactory


class BlogFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    title = Sequence(lambda n: 'user{0}'.format(n))
    description = factory.fuzzy.FuzzyText('this is my first blog')
    user_id = factory.SubFactory(UserFactory)
    blog_created_on = factory.LazyFunction(datetime.datetime.now)