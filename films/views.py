from django.db.models import Q
from django.views.generic import ListView, DetailView
from films.models import Film, Genre

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