# documents/forms.py
from django import forms
from .models import Document, DocumentEvaluation

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'year_of_publication', 'keywords', 'file', 'document_type', 'author', 'field', 'genre']

class DocumentEvaluationForm(forms.ModelForm):
    class Meta:
        model = DocumentEvaluation
        fields = ['comment']
