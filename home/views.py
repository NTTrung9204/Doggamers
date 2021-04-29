
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
# Create your views here.
def index(request):
   return render(request, 'pages/home.html')
def contact(request):
   return render(request, 'pages/contact.html')
def game1(request):
   return render(request, 'pages/game1.html')
def game2(request):
   return render(request, 'pages/game2.html')
def game3(request):
   return render(request, 'pages/game3.html')
def game4(request):
   return render(request, 'pages/game4.html')
def game5(request):
   return render(request, 'pages/game5.html')
def game6(request):
   return render(request, 'pages/game6.html')
def game7(request):
   return render(request, 'pages/game7.html')
def game8(request):
   return render(request, 'pages/game8.html')
def game9(request):
   return render(request, 'pages/game9.html')
def game10(request):
   return render(request, 'pages/game10.html')
def about2048(request):
   return render(request, 'pages/about2048.html')
def aboutAstray(request):
   return render(request, 'pages/aboutAstray.html')
def aboutBomb(request):
   return render(request, 'pages/aboutBomb.html')
def aboutFlappybird(request):
   return render(request, 'pages/aboutFlappybird.html')
def aboutHexGL(request):
   return render(request, 'pages/aboutHexGL.html')
def aboutHextris(request):
   return render(request, 'pages/aboutHextris.html')
def aboutMario(request):
   return render(request, 'pages/aboutMario.html')
def aboutPuzzles(request):
   return render(request, 'pages/aboutPuzzles.html')
def aboutSnake(request):
   return render(request, 'pages/aboutSnake.html')
def aboutTrex(request):
   return render(request, 'pages/aboutTrex.html')
def login(request):
   return render(request, 'pages/login.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})

