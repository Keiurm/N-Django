from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if "message" in request.GET and "title" in request.GET:
        title, message = request.GET["title"], request.GET["message"]
        params = {
            "title": title,
            "message": message,
        }

    else:
        params = {
            "title": "Hello Django!",
            "message": "これはサンプルで作った hello のページです",
        }
    params["goto"] = "next"
    params["numbers"] = range(5)
    params["items"] = ["apple", "tomato", "banana", "melon"]
    return render(request, "hello/index.html", params)


def next(reqest):
    params = {
        "title": "hello/next",
        "message": "これはサンプルで作った next のページです",
        "goto": "index",
    }
    return render(reqest, "hello/index.html", params)
