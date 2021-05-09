from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.shortcuts import render
import os


def workspace(request):
    ls = os.popen("ls database/workspace").read()
    if request.method == "GET":
        return render(request, "root/workspace/workspace.html", {"files": ls})

    elif request.method == "POST":
        try:
            f = request.GET["file"]
            return HttpResponse(open("database/workspace/" + f, "rb"))
        except MultiValueDictKeyError:
            e = request.FILES
            for w in e.getlist("file"):
                with open("database/workspace/" + request.GET["name"], "wb") as ftw:
                    ftw.write(w.read())
            open("database/file_db.txt", "w").write(ls)
            return render(request, "root/workspace/workspace.html", {"file_name": "file_name", "files": ls})


def index(request):
    return render(request, "root/workspace/index.html")

