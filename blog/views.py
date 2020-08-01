from django.shortcuts import render, get_object_or_404
from .models import Entry, Comment, Answer

def all_entries(request):
    entries = Entry.objects.order_by('-created_at')
    return render(request, 'blog/all_entries.html', {'entries':entries})

def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    comments = Comment.objects.filter(parent_entry=entry_id)
    print("COMMENTS:\n")
    for comment in comments:
        print(comment)
    return render(request, 'blog/detail.html', {
        'entry':entry,
        'comments': comments
        })
