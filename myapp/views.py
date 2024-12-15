from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    html = f'''
        <h1>Home</h1>
        <div style="margin-top: 40px;">
            This page is home page!!
        </div>
    '''

    return HttpResponse(html)
