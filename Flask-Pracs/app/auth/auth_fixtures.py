from ..auth.auth_factories import UserFactory
from . import factory

def create_auth_fixtures():
    factory.UserFactory.create_batch(size=50)

    # Let's create a few, known objects.
    factory.UserFactory(
        name='Shruti',
        username='shrutih',
        email='shruti.hiremath@cuelogic.com',
        password='12345',
        address='Pune',
        contact=6444976544,
        gender='Female',
    )
