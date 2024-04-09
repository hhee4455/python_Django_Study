from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def some_url(request):
    return HttpResponse("some_url을 구현해 봤습니다.")