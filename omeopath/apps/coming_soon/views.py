from django.views.generic.edit import BaseCreateView
from django.http import HttpResponse
from models import Prospect

# Create your views here.

class CreateProspect(BaseCreateView):
    """View for notification signup function"""
    model = Prospect
    
    def form_invalid(self, form):
        return HttpResponse(form.errors.as_ul())
        
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(status=201)
        
