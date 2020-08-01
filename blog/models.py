from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    commenter = models.CharField(max_length=40)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

class Answer(models.Model):
    commenter = models.CharField(max_length=40)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
