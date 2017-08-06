from django.http import HttpResponse
def index(request):
    return HttpResponse("Inside Code Tracker")
