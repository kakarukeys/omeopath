from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic.edit import BaseCreateView
from django.views.generic import TemplateView

from paypal.standard.ipn.signals import payment_was_successful

from models import Prospect
from forms import DonationForm

BOOK_NAME = "50 Things About GERD Your Doctor Did Not Tell You"

# Create your views here.

class CreateProspect(BaseCreateView):
    """View for notification signup function"""
    model = Prospect
    
    def form_invalid(self, form):
        return HttpResponse(form.errors.as_ul())
        
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(status=201)
        
class ComingSoon(TemplateView):
    template_name = "coming_soon/coming_soon.html"
    
    def get_context_data(self, **kwargs):
        """retrieve the context variable and put paypal form into it"""
        context = super(ComingSoon, self).get_context_data(**kwargs)
        
        get_url = lambda name: self.request.build_absolute_uri(reverse(name))
        
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "item_name": BOOK_NAME,
            "invoice": "GB-00009",
            "amount": "35.00",
            "notify_url": get_url("paypal-ipn"),
            "return_url": get_url("paypal-pdt"),
            "cancel_return": get_url("coming_soon"),
        }
        form = DonationForm(initial=paypal_dict)
        
        context["donate_button"] = form.sandbox() if settings.PAYPAL_TEST else form.render()
        return context
        
def act_after_receiving_payment(sender, **kwargs):
    """stub"""
    print "hahaha in signal"      
    print sender    
payment_was_successful.connect(act_after_receiving_payment)

