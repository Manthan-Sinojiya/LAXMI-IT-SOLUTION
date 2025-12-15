from django.shortcuts import render
from .forms import ContactForm, FeedbackForm

def index(request):
    contact_form = ContactForm()
    feedback_form = FeedbackForm()

    if request.method == "POST":
        if "contact_submit" in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
        elif "feedback_submit" in request.POST:
            feedback_form = FeedbackForm(request.POST)
            if feedback_form.is_valid():
                feedback_form.save()

    return render(request, "index.html", {
        "contact_form": contact_form,
        "feedback_form": feedback_form
    })
