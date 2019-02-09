from django.http import HttpResponse


def home(request):
    return HttpResponse('<!DOCTYPE html> <html> <body> <h1> <center>Custom User Model</center> </h1> </body> </html>')
