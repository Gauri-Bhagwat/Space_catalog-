from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Note, SpaceObject

from .forms import NoteForm
def home(request):
    return render(request, 'catalog/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'catalog/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('spaceobject_list')
    else:
        form = AuthenticationForm()
    return render(request, 'catalog/login.html', {'form': form})

@login_required
def spaceobject_list(request):
    objects = SpaceObject.objects.all()
    return render(request, 'catalog/spaceobject_list.html', {'objects': objects})

@login_required
def spaceobject_detail(request, id):
    obj = get_object_or_404(SpaceObject, id=id)
    return render(request, 'catalog/spaceobject_detail.html', {'object': obj})


# Notes List View
def notes_list(request, id):
    spaceobject = get_object_or_404(SpaceObject, id=id)
    notes = spaceobject.notes.all()
    return render(request, 'catalog/notes_list.html', {'spaceobject': spaceobject, 'notes': notes})

# Create Note
def create_note(request, id):
    spaceobject = get_object_or_404(SpaceObject, id=id)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.spaceobject = spaceobject
            note.save()
            return redirect('notes_list', id=spaceobject.id)
    else:
        form = NoteForm()
    return render(request, 'catalog/note_form.html', {'form': form, 'spaceobject': spaceobject})

# Update Note
def update_note(request, id, note_id):
    spaceobject = get_object_or_404(SpaceObject, id=id)
    note = get_object_or_404(Note, id=note_id, spaceobject=spaceobject)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_list', id=spaceobject.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'catalog/note_form.html', {'form': form, 'spaceobject': spaceobject})

# Delete Note
def delete_note(request, id, note_id):
    spaceobject = get_object_or_404(SpaceObject, id=id)
    note = get_object_or_404(Note, id=note_id, spaceobject=spaceobject)
    if request.method == "POST":
        note.delete()
        return redirect('notes_list', id=spaceobject.id)
    return render(request, 'catalog/note_confirm_delete.html', {'note': note, 'spaceobject': spaceobject})


