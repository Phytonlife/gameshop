from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models import Count, Sum, Avg, Max, Min

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse('game_detail', args=[self.slug])

    def __str__(self):
        return f'{self.title}'

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)


class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    fio = models.CharField(max_length=255)
    subjects = models.ManyToManyField('Subject', blank=True, related_name='subs')