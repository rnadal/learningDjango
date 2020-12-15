from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code

def contact_view(request, *args, **kwargs):
    # dict for variables we want to pass to the template
    my_context = {
        "some_text": "this is a new text",
        "some_number": 0,
        "list": [123,456,789]
    }
    return render(request, "contact.html", my_context)
    # return HttpResponse("<h1>Contact Page</h1>") # string of HTML code