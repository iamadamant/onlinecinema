from django.contrib.auth.models import User
from django.db.models import Q
from django.http import QueryDict
from django.views.generic import ListView, DetailView

from films.models import Film, Genre, Comment
from django.http.response import HttpResponse
from django.views.generic import View
from django.core import serializers
from films.forms import *
from django.utils.html import escape
# Create your views here.


class FilmsView(ListView):
    model = Film
    template_name = 'films/films.html'


class SearchView(ListView):
    model = Film
    template_name = 'films/searched_films.html'

    def get_queryset(self):
        search = self.request.GET.get('search', '').lower()
        return self.model.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))


class FilmView(DetailView):
    model = Film
    template_name = 'films/film_detail.html'
    slug_field = 'id'
    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        comments = self.object.comments.filter(parent__isnull=True)
        context = super().get_context_data()
        context['comments'] = comments
        return context


class FilmCommentsView(View):

    def put(self, request, pk, *args, **kwargs):
        author_id = request.GET.get('author')
        film = Film.objects.get(pk=pk)
        author = User.objects.get(pk=author_id)
        User.natural_key = lambda x: (x.id, x.username)
        PUT = QueryDict(request.body.decode('utf-8'))
        body_text = PUT.getlist('body', None)[0]
        parent_id = PUT.getlist('parent', None)[0]
        form = AddCommentForm({'body': body_text})
        if form.is_valid():
            body = escape(form.cleaned_data['body'])
            parent = None
            if parent_id != '':
                parent = Comment.objects.get(pk=parent_id)
            Comment.objects.update_or_create(film=film, author=author, parent=parent, defaults={'body': body})
            comments = film.comments.all()
            data = serializers.serialize('json', comments, use_natural_foreign_keys=True)
            return HttpResponse(data, content_type='application/json')


