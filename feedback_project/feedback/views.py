# feedback/views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

def thank_you(request):
    return render(request, 'feedback/thank_you.html')

# Add this home view for the root URL
def home(request):
    return render(request, 'feedback/home.html')
