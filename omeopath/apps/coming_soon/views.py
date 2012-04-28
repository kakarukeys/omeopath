from django.shortcuts import render_to_response

# Create your views here.

def coming_soon(request):
    return render_to_response('coming_soon.html')
    
