from django.shortcuts import render
import os


# os.popen("ngrok http 80 --log smtp/ng_link")
# print(os.system("pwd"))
# with open("smtp_tmp/ng_link") as ngf:
#     ng_link = ngf.read().split("url="[1].split("\n")[0])
#     print("\n" * 20)
#     print(ng_link)


def index(request):
    return render(request, "smtp/smtp.html")
