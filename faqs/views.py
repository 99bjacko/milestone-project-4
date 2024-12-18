from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Faq
from .forms import FaqForm


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
        messages.error(
            request, 'Sorry, only store administrators can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added FAQ!')
            return redirect(reverse('faqs'))
        else:
            messages.error(
                request, 'Failed to add FAQ. Please ensure the form is valid.')
    else:
        form = FaqForm()

    template = 'faqs/add_faq.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_faq(request, faq_id):
    """ Add an existing FAQ """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store administrators can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated FAQ.')
            return redirect(reverse('faqs'))
        else:
            messages.error(
                request,
                'Failed to update FAQ. Please ensure the form is valid.')

    else:
        form = FaqForm(instance=faq)
        messages.info(request, f'You are editing {faq.question}')

    template = 'faqs/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """ Delete an existing FAQ """
    faq = get_object_or_404(Faq, pk=faq_id)
    faq.delete()
    messages.success(request, 'FAQ deleted successfully.')
    return redirect(reverse('faqs'))
