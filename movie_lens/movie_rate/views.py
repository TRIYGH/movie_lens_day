from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Movie, Rater, Rating


def index(request):
    movie_list = Movie.objects.order_by('-title')[:11]
    context = {'movie_list': movie_list}
    return render(request, 'movie_rate/index.html', context)


def detail(request, movie_id):
    a_movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie_rate/detail.html', {'a_movie': a_movie})


def rater_view(request, rater_id):
    # print(request.POST)
    dude = Rater.objects.all()
    context = {'dude': dude}
    return render(request, 'movie_rate/rater_view.html', context)

def movie_view(request, movie_id):
    a_movie = Movie.objects.all()
    context = {'a_movie': a_movie}
    return render(request, 'movie_rate/movie_view.html', context)

def rating_view(request, rating_id):
    ratings = Rating.objects.all()
    context = {'ratings': ratings}
    return render(request, 'movie_rate/rating_view.html', context)

def top20_view(request):
    top_movie_list = Rating.top_movies(20)
    context = {'top_movie_list': top_movie_list}
    return render(request, 'movie_rate/top20_view.html', context)

def movie_detail_view(request):
    this_movie = 111 #ask for this
    m = Movie.objects.filter(pk=this_movie)
    for each in m: #bc it will not get out of query form
        mv = m
    movie_detail = Rating.get_ratings_of_specific_movie(this_movie)
    avg_rate = Rating.individual_movie_avg_rating(this_movie)
    context = {'movie_detail': movie_detail,
                'avg_rate': avg_rate,
                'mv': mv}
    return render(request, 'movie_rate/movie_detail_view.html', context)


# def index(request):
#     movie_list = Movie.objects.order_by('-title')[:11]
#     output = ', '.join([m.title for m in movie_list])
#     return HttpResponse(output)

# def index(request):
#     return HttpResponse("<h1>Hello, world. You're at the movie_rate index.</h1>")
    # return render(request, 'folder/index.html') use this soon !!
    #  and remove the $ from the urls.py file in the app folder

    #return render(request, 'folder/index.html', context)
    #   context adds {} like a .format in print
    #       you put those {} in your html files
#=============================================================
# def movie_view(request, movie_id):
#     return HttpResponse("You're looking at %s." % movie_id)
#
# def rater_view(request, rater_id):
#     response = "You're looking at the results of Rater: %s."
#     return HttpResponse(response % rater_id)
#
# def rating_view(request, rating_id):
#     return HttpResponse("You're looking at ratING view:  %s." % rating_id)
