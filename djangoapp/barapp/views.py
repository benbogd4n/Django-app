from django.shortcuts import render

# Create your views here.
def barapp_main(request):
    return render(request, 'barapp/bar.html')
