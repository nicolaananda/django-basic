from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

# agar title yang diinputkan menjadi title di admin
    def __str__(self):
        return self.title
    
class Task(models.Model):
    task = models.CharField(blank=True, null=True, max_length=250)
    is_done = models.BooleanField(default=False)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
