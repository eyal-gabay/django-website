from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    if request.method == "GET":
        return render(request, "register/login.html", status=200)

    elif request.method == "POST":
        if request.POST["user"] != "" and request.POST["pass"] != "":
            with open("database/data.txt", "a") as file:
                lou = []
                for user in open("database/data.txt").read().splitlines():
                    lou.append(user.split(" ")[0])
                if not request.POST["user"] in lou:
                    for c in range(len("!$+-()@<>.")):
                        if "!$+-()@<>. "[c] in request.POST["user"]:
                            return render(request, "register/register_null.html", status=200)
                    file.write(request.POST["user"] + " " + request.POST["pass"] + "\n")
                    return render(request, "register/good.html", status=200)
                else:
                    return render(request, "register/register_null.html", status=200)
        else:
            return render(request, "register/register_null.html", status=200)


def log_out(request):
    httpr = HttpResponse("<script>window.location = \"/\"</script>")
    httpr.delete_cookie("key")
    return httpr


def re(request):
    return HttpResponse("hi", status=303)
