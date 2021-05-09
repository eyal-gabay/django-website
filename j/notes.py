from django.shortcuts import render
from django.http import JsonResponse
import json


def main(request):
    e = "6n5s6n5sn5r8,6f9078)gf6ab4666sm754sm754sm854s1"
    if request.method == "GET":
        return render(request, "j/notes.html")

    elif request.method == "POST":
        print(request.body)
        parameters = json.loads(request.body)
        print(parameters)
        if parameters["page_number"] == e:
            print("1")
        return render(request, "j/notes.html", {"f": "eeeee"})

