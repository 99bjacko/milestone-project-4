from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Faq
from .forms import FaqForm

# Create your views here.

def all_faqs(request):
    """ A view to show all frequently asked questions """

    faqs = Faq.objects.all()
    context = {
        'faqs': faqs,
    }

    return render(request, 'faqs/faqs.html', context)

@login_required
def add_faq(request):
    """ Add a frequently asked question to the FAQs page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store administrators can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added FAQ!')
            return redirect(reverse('faqs'))
        else:
            messages.error(request, 'Failed to add FAQ. Please ensure the form is valid.')
    else:
        form = FaqForm()

    template = 'faqs/add_faq.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
