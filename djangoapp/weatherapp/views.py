from django.shortcuts import render

# Create your views here.
def weatherapp_main(request):
    return render(request, 'weatherapp/weather.html')
