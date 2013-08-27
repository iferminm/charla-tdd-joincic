#coding=utf-8
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.core import mail
from django.contrib.auth.models import User
from .models import *
from .factories import *
import mocker

class RegistroTest(TestCase):
    def setUp(self):
        self.post_data = {
            'first_name': 'Israel',
            'last_name': 'Fermin',
            'username': 'iferminm',
            'email': 'iferminm@gmail.com',
            'password': '1234',
            'password2': '1234',
            'address': 'Lorem ipsum... bla bla',
            'sex': 'm',
            'telephone': '2129870091'
        }
        self.client = Client()

    def test_registro_ok(self):
        total_usuarios = User.objects.count()
        emails = len(mail.outbox)
        k = {'user_type': 'user'}
        response = self.client.post(reverse('registro', kwargs=k), self.post_data) 
        self.assertEquals(User.objects.count(), total_usuarios + 1)
        user = User.objects.get(email=self.post_data['email'])
        self.assertFalse(user.is_active)
        self.assertEquals(UserProfile.objects.count(), 1)


class PremioTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserFactory()
        self.post_data = {'text': 'Esta pelicula es genial'}
        self.movie = MovieFactory()
        self.movie.save()
        self.client.login(username=self.user.username, password='1234')

    def test_premio(self):
        from django.utils import simplejson
        m = mocker.Mocker()
        obj = m.replace('random')
        obj.randint(1, 200)
        m.result(22)
        k = {'movie_id': self.movie.id}
        m.replay()

        response = self.client.post(reverse('add_review', kwargs=k), self.post_data)

        self.assertEquals(response.status_code, 201)
        self.assertEquals(self.movie.moviereview_set.count(), 1)
        d = simplejson.loads(response.content)

        self.assertTrue(d.has_key('premio'))

