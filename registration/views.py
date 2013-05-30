#coding=utf-8
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *
from .models import *

def register_user(request, user_type):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.process()
            return HttpResponse(status=201)
        return HttpResponse(status=400)
    return HttpResponse(status=403)


def validate_user(request):
    pass

def list_users(request, user_type):
    pass

def view_user(request, user_id):
    pass

def edit_user(request, user_id): 
    pass

def add_comment(request, target_review):
    pass

def get_comments(request, review):
    pass

@login_required
def add_review(request, movie_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            from django.utils import simplejson
            import random
            user = request.user
            movie = Movie.objects.get(id=movie_id)
            r = MovieReview(user=user, movie=movie)
            r.text = form.cleaned_data['text']
            r.save()
            n = random.randint(1, 200)
            data = {'premio': 'entrada al cine'} if not n % 11 else {}
            result = simplejson.dumps(data)
            return HttpResponse(content=result, status=201)
        return HttpResponse(status=400)
    return HttpResponse(status=403)

def add_movie(request):
    pass


