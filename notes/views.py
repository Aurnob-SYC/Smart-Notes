from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Note

@login_required
def feature_notes(request):
    return render(request, 'notes.html')

@login_required
def create_notes(request):
    print("create_notes view called")  # <- debug
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        print("title:", title, "content:", content)  # <- debug
        if title and content:
            note = Note.objects.create(title=title, content=content)
            note.users.add(request.user)
            print("note saved:", note.id)  # <- debug
            return JsonResponse({"success": True, "message": "Note created successfully!"})
        else:
            return JsonResponse({"success": False, "message": "Title and content cannot be empty."})
    
    return render(request, 'notes/create_notes.html')


@login_required
def my_notes(request):
    notes = Note.objects.filter(users=request.user).order_by('-updated_at')
    return render(request, 'notes/my_notes.html', {'notes': notes})
