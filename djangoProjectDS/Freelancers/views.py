from django.shortcuts import render



def home(request):
    return render(request, 'templates/homepage.html')
def form(request):
    return render(request, 'templates/form.html')