from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class MainPageView(View):
    def get(self, request):
        return render(request, 'main.html')
    
class ContactPageView(View):
    def get(self, request):
        # return render(request, 'djangoApp/contact.html')
        return render(request, 'contact.html')
    
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse(f"Form Submitted! Name: {name}, Email: {email}, Message: {message}")
    
class AboutPageView(View):
    def get(self, request):
        # return render(request, 'djangoApp/about.html')
        return render(request, 'about.html')
        
