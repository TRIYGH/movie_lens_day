from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=300)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)

    def get_ratings_of_specific_rater(requested_rater):
        all_ratings = Rater.objects.all(id=requested_rater)
        return all_ratings


class Rating(models.Model):
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    timestamp = models.DateTimeField('date rated')

    def __str__(self):
        return str(self.rating)

    # def movie_avg_rating():



    def get_ratings_of_specific_movie(requested_movie):
        all_movies = Movie.objects.all(movie=requested_movie)
        return all_movies

    def top_movies(num):
        avg = []
        top = []
        top_10_movies = Movie.objects.all()
        for each in top_10_movies:
            avg.append(mean(sum(get_ratings_of_specific_movie(each))))
        avg.sort(reverse=True)
        for i in range(num):
            top.append(avg[i])
        return top
