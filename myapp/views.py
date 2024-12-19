from django.shortcuts import render, HttpResponse

from .models import People

# Create your views here.
def home(request):

    person = People.objects.get(name="this is my name")
    html = f'''
        <h1>Home</h1>
        <div style="margin-top: 40px;">
            This page is home page!!
            {person.name}
        </div>
    '''

    return HttpResponse(html)
