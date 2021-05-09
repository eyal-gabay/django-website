from django.urls import path, include
from django.http import HttpResponse
import random


def not_found(request, exception=None):
    stat = [200, 302]
    all = "zxc vbnm,./asdfg hjkl;'qw ertyui op[\n]12345 60-=Z XCVBNM<>?AS D FGHJKL:\"QWE RTYUIOP{}! @#$%^& *()_+"
    r = ""
    for i in range(random.randrange(5000)):
        for word in random.choice(all):
            r += word
            if random.randrange(5) == 4:
                r += "<br>"
    return HttpResponse(r, status=random.choice(stat))


handler404 = not_found

urlpatterns = [
    path("q/", include("q.urls")),
    path("", include("root.urls")),
    path("register/", include("register.urls")),
    path("smtp/", include("smtp.urls")),
    path("j/", include("j.urls")),
]

