#coding=utf-8
from django.db import models
from django.contrib.auth.models import User


SEX_CHOICES = (
    ('f', 'Female'),
    ('m', 'Male',),
)
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.URLField()
    address = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    telephone = models.CharField(max_length=32)
    cel_phone = models.CharField(max_length=32, blank=True, null=True)

    def __unicode__(self):
        return self.user.username


def RegistrationProfile(models.Model):
    user = models.OneToOneField(User)
    token = models.CharField(max_length=32)
    encoded = models.CharField(max_length=256)

    def __unicode__(self):
        return self.user.username


class ActionShoot(models.Model):
    image = models.ImageField(upload_to='action_shoots')
    thumbnail = models.ImageField(upload_to='action_shoots_thumbs')
    caption = models.CharField(max_length=140)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.caption


class ActorProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='actor_profile_pictures')
    avatar_thumbnail = models.ImageField(upload_to='actor_profile_pictures_thumbs')
    action_shoots = models.ManyToManyField(ActionShoot)
    bio = models.TextField(blank=True, null=True)
    likes = models.TextField(blank=True, null=True)
    dislikes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.user.full_name
        

class MovieSample(models.Model):
    image = models.ImageField(upload_to='movie_samples')
    thumbnail = models.ImageField(upload_to='movie_samples_thumbs')
    caption = models.CharField(max_length=140, blank=True, null=True)
 
    def __unicode__(self):
        return self.caption


class Movie(models.Model):
    actors = models.ManyToManyField(User)
    title = models.CharField(max_length=64)
    description = models.TextField()

    def __unicode__(self):
        return self.title


class MovieReview(models.Model):
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie)
    text = models.TextField()

    def __unicode__(self):
        return self.text[:140]


class Comment(models.Model):
    user_from = models.ForeignKey(User)
    review = models.ForeignKey(MovieReview)
    when = models.DateTimeField()
    text = models.TextField()

    def __unicode__(self):
        return self.text[:140]


class Prize(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    qty = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s | %s' % (self.name, self.qty)
