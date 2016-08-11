from django.db import models


class Movie(models.Model):
    # movieID = models.IntegerField(default=0)
    title=models.CharField(max_length=300)
    genre = models.CharField(max_length=50)


class User(models.Model):
    # userID = models.IntegerField(max_length=9)
    gender = models.CharField(max_length=1)
    age = models.IntegerField(max_length=2)
    occupation = models.IntegerField()
    zipcode = models.CharField(max_length=10)
    

class Rating(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    movieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(max_length=1)
    timestamp = models.DateTimeField('date rated')
