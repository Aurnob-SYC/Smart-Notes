from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def feature_notes(request):
    return render(request, 'notes.html')

@login_required
def create_notes(request):
    return render(request, 'notes/create_notes.html')

@login_required
def my_notes(request):
    return render(request, 'notes/my_notes.html')