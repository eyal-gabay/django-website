from django.shortcuts import render
from django.http import HttpResponse


def login(self):
    pass
    # coolies = self.COOKIES
    #
    # def check_cookie(request):
    #     if 1:
    #         return self(request)
    #     else:
    #         return HttpResponse(status=500)
    # return check_cookie


@login
def index(request):
    return render(request, "j/j.html")

