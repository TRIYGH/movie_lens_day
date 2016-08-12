from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Hello, world. You're at the movie_rate index.</h1>")
    # return render(request, 'folder/index.html') use this soon !!
    #  and remove the $ from the urls.py file in the app folder

    #return render(request, 'folder/index.html', context)
    #   context adds {} like a .format in print
    #       you put those {} in your html files
