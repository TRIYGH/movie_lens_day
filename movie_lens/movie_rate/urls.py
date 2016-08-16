from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^movie/(?P<movie_id>[0-9]+)/$', views.movie_view, name='movie_view'),
    # ex: /polls/5/results/
    url(r'^rater/(?P<rater_id>[0-9]+)/$', views.rater_view, name='rater_view'),
    # ex: /polls/5/vote/
    url(r'^rating/(?P<rating_id>[0-9]+)/$', views.rating_view, name='rating_view'),

    url(r'^top/$', views.top20_view, name='top20_view'),

    url(r'^detail/$', views.movie_detail_view, name='movie_detail_view'),

]
