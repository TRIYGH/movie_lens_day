from django.db import models
# from movie_rate.models import Movie, Rater, Rating

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

    def individual_movie_avg_rating(which_movie):
        total_rate = 0
        the_movie = Rating.objects.filter(movie_id=which_movie)

        for each in the_movie:
            total_rate += each.rating
        try:
            ind_rating = total_rate/len(the_movie)
        except:
            ind_rating = 0

        if len(the_movie) < 20:
            ind_rating = .01
        return (ind_rating)

    def get_ratings_of_specific_movie(requested_movie):
        all_ratings = Rating.objects.filter(movie_id=requested_movie)
        return all_ratings

    def top_movies(num):
        averages = []
        top = []
        top_movies = Movie.objects.all().count()
        for i in range(top_movies):
            avg = Rating.individual_movie_avg_rating(i+1)
            averages.append((avg, i+1))
            print("\n"*50)
            c = (i+1) / 1683
            print("Percentage complete:  ",c, "%")
        averages.sort(reverse=True)
        for i in range(num):
            top.append(averages[i])
        return top      # returns list of TUPLES !
