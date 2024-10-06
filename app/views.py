from django.shortcuts import render
from .models import Category, Slider, About, Appconf
# Create your views here.

def home(request):
   categories = Category.objects.all()  # Tüm kategorileri al
   
   context = {
      'categories': categories  # Template'e gönderilecek veriler
   }
   return render(request, 'pages/home.html', context)

def events(request):
   sliders = Slider.objects.all()
   
   context = {
      'sliders': sliders
   }
   return render(request, 'pages/events.html', context)

def about(request):
   abouts = About.objects.all()
   context = {
      'abouts': abouts
   }
   return render(request, 'pages/about.html', context)

def contact(request):
   contacts = Appconf.objects.all()

   contact_data = {
      'email': 'example@example.com',
      'telefon': '123456789',
      'adress': 'geo:39.9334,32.8597',
   }
   context = {
      'contacts': contacts
   }
   return render(request, 'pages/contact.html', context)

def test(request):
   return render(request, 'test.html')