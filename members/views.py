from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")
def players(request):
    return render(request,"players.html")
def gallery(request):
    return render(request,"gallery.html")
def fixture(request):
    return render(request,"fixture.html")

    


