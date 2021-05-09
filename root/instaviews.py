from django.http import HttpResponse
from database.hash import ehash


def main(request):
    if request.COOKIES.get("key"):
        key = ehash.decode("hW$%kLlK)_xH")
        for line in open("database/data.txt").read().splitlines():
            if key == line:
                return HttpResponse(key + " " + line)
    return HttpResponse("u need to connect")