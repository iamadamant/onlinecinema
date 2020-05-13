from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=32, verbose_name='Genres name')

    def __str__(self):
        return str(self.name)

class Film(models.Model):
    title = models.CharField(max_length=128, verbose_name='Title')
    poster = models.ImageField(upload_to='', verbose_name='Poster')
    description = models.TextField(max_length=256, verbose_name='Description')
    rating = models.PositiveSmallIntegerField(blank=True)
    duration = models.DurationField(verbose_name='Duration')
    genres = models.ManyToManyField(Genre, related_name='films', verbose_name='Genres')

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('film_detail_url', kwargs={'pk': self.pk})



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='childs')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=4096)

    def __str__(self):
        return 'Film:'+str(self.film)+' by:'+str(self.author)