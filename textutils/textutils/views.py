

from django.http import HttpResponse


# def index(request):
#     return HttpResponse('''<h2>Heading he ye </h2> <a href="https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww"> Code With Harry </a>     <a href="https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww"> Code With Harry </a>''')

def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("Remove punc")

def capfirst(request):
    return HttpResponse("capitalfirst")

# def about(request):
#     with open("one.txt", "r+") as f:
#         a = f.read()
#     return HttpResponse(a)