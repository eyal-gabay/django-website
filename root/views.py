from django.http import HttpResponse
from django.shortcuts import render
from root import database
from database.hash import ehash
from pprint import pprint
import random


def index(request):
    # do nothing line
    # print("-" * 120)
    # pprint(request.META)
    request.session['membeer_id'] = "riamine"
    if request.method == "GET":
        if request.COOKIES.get("key"):
            key = ehash.decode("hW$%kLlK)_xH")
            for line in open("database/data.txt").read().splitlines():
                if key == line:
                    response = render(request, 'root/noobs.html', {"user": line.split(" ")[0],
                                                                   "key": request.COOKIES.get("key"),
                                                                   "headers": request.headers,
                                                                   "meta": request.META})
                    return response
        data = {
            "ip": request.META["REMOTE_ADDR"],
        }

        r = render(request, 'root/root.html', data)
        random_cookie = str(int(repr(random.random())[2:]))
        r.set_cookie("best_cookie_ever", random_cookie)
        r.set_cookie("ip", data["ip"])
        r.status_code = 404
        r["Date"] = "now"
        r["Server"] = "eyal gabays server :)"
        r["X-Frame-Options"] = "its a good website, dont u think so?"
        return r
    elif request.method == "POST":
        did_he = [False, None]
        try:
            for w in open("database/data.txt").read().splitlines():
                if request.POST["user"] == w.split(" ")[0] and request.POST["pass"] == w.split(" ")[1]:
                    did_he[0], did_he[1] = True, request.POST["user"]
                    break
            if did_he[0]:
                login_data = {
                    "user": request.POST["user"],
                    "key": ehash.encode(request.POST["user"] + " " + request.POST["pass"]),
                }
                noob_login = render(request, 'root/noobs.html', login_data)
                noob_login.set_cookie("key", login_data["key"])
                del noob_login["Server"]
                return noob_login
            try:
                if "'" in request.POST["user"] or "'" in request.POST["pass"]:
                    return HttpResponse("error 500<br>")
                elif request.POST["pass"] == database.usernames[request.POST["user"]]:
                    return render(request, 'root/eyal.html')
                else:
                    return render(request, 'root/root_incorrect_password.html')
            except (ValueError, KeyError):
                return render(request, 'root/root_incorrect_password.html')
        except:
            key = ehash.decode(request.POST["key"])
            for line in open("database/data.txt").read().splitlines():
                if key == line:
                    return render(request, 'root/noobs.html', {"user": line.split(" ")[0], "key": request.POST["key"]})
            return render(request, 'root/incorrect_key.html')



