from django.shortcuts import render

# Create your views here.
def intropage(request):
    return render(request, 'introduction.html')