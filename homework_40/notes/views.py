from django.shortcuts import render

from .models import Note


def notes_list(request):
    notes = Note.objects.select_related('category').all()
    context = {'notes': notes}
    return render(request, 'notes/index.html', context)