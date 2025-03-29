from django.shortcuts import render
from django.http import HttpResponse
from .forms import TutorialForm


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


def form(request):
    params = {
        "title": "Form",
        "msg": "メッセージを入力してください。",
    }
    return render(request, "hello/form.html", params)


def form_result(request):
    msg = request.POST["msg"]
    params = {
        "title": "Form",
        "msg": msg,
    }
    return render(request, "hello/form.html", params)


def new_form(request):
    params = {
        "title": "BMI計算機",
        "form": TutorialForm(),
    }
    if request.method == "POST":
        weight = request.POST["weight"]
        height = request.POST["height"]

        # cmからmに変換
        height = float(height) / 100
        # BMI計算
        bmi = float(weight) / (height**2)
        # BMIを四捨五入
        bmi = round(bmi, 1)
        # BMIを表示
        params["bmi"] = bmi
        # フォームを表示
        params["form"] = TutorialForm(request.POST)
    return render(request, "hello/new_form.html", params)
