
from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    DOC_TYPES = (
        ('book', 'Book'),
        ('newspaper', 'Newspaper'),
        ('project', 'Project'),
        
    )
    name = models.CharField(max_length=255)
    year_of_publication = models.IntegerField()
    keywords = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    document_type = models.CharField(choices=DOC_TYPES, max_length=20)
    author = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DocumentEvaluation(models.Model):
    document = models.ForeignKey(Document, related_name='evaluations', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f'Comment by {self.user.username} on {self.document.name}'
