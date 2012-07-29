from django.utils.safestring import mark_safe
from paypal.standard.conf import POSTBACK_ENDPOINT, SANDBOX_POSTBACK_ENDPOINT
from paypal.standard.forms import PayPalPaymentsForm

class DonationForm(PayPalPaymentsForm):
    """Paypal payment form but using our own buttons"""
    
    def render(self):
        return mark_safe(u"""<form action="%s" method="post">
    %s
    <button class="btn btn-primary" name="submit">Donate <i class="icon-leaf icon-white"></i></button>
</form>""" % (POSTBACK_ENDPOINT, self.as_p()))
        
    def sandbox(self):
        return mark_safe(u"""<form action="%s" method="post">
    %s
    <button class="btn btn-primary" name="submit">Donate <i class="icon-leaf icon-white"></i></button>
</form>""" % (SANDBOX_POSTBACK_ENDPOINT, self.as_p()))

