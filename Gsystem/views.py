from django.shortcuts import render

def home(request):
    return render(request, 'Gsystem/home.html', {})

# Create your views here.
