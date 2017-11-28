from ..blog_mod.blog_factories import BlogFactory
from . import factory


def create_blog_fixtures():
    factory.BlogFactory.create_batch(size=50)

    # Let's create a few, known objects.
    factory.BlogFactory(
        title='Blog1',
        description='This is my first blog',
    )
