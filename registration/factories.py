#coding=utf-8
from django.contrib.auth.models import User
from .models import *
import factory

class UserFactory(factory.Factory):
    FACTORY_FOR = User

    username= factory.Sequence(lambda n: 'Foo%s' % n)
    first_name = factory.Sequence(lambda n: 'Foo%s' % n)
    last_name = 'Bar'
    email = factory.LazyAttribute(lambda obj: '%s@dom.com' % obj.first_name.lower())

    @classmethod
    def _prepare(cls, create, *args, **kwargs):
        user = super(UserFactory, cls)._prepare(create, *args, **kwargs)
        user.set_password('1234')

        if create:
            user.save()

        return user

class MovieFactory(factory.Factory):
    FACTORY_FOR = Movie

    title = factory.Sequence(lambda n: 'Duro de Matar %s' % n)
    description = 'Un gran lorem ipsum'

