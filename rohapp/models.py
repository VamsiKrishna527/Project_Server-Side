from django.db import models

# Create your models here.

class Actors(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=30, blank=True)
    marital_status = models.BooleanField(default=False)
    spouse = models.CharField(max_length=100, blank=True)
    parents = models.CharField(max_length=100, blank=True)
    siblings = models.CharField(max_length=200, blank=True)
    upcoming_movie = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=400, blank=True)
    picture_url = models.URLField(blank=True, null=True)

    def  __str__(self):
        return self.name
    @property
    def age(self):
        from datetime import date
        today = date.today()
        born = self.birthdate
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
class Movies(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, blank=True)
    rating = models.CharField(max_length=10, blank=True)
    release_date = models.DateField(blank=True, null=True)
    budget = models.CharField(max_length=20, blank=True, null=True, help_text="In dollars")
    collections = models.CharField(max_length=20, blank=True, null=True, help_text="In dollars")
    actor = models.ForeignKey(Actors, related_name='movies', on_delete=models.CASCADE)

    def __str__(self):
        return self.title