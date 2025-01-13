from django.contrib import admin
from .models import Document, DocumentEvaluation


class DocumentEvaluationInline(admin.TabularInline):
    model = DocumentEvaluation
    extra = 1  # Number of empty forms to display by default

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'document_type', 'year_of_publication', 'field')
    search_fields = ('name', 'author', 'keywords', 'field', 'genre')
    list_filter = ('document_type', 'field', 'genre')
    inlines = [DocumentEvaluationInline]
admin.site.register(Document)
admin.site.register(DocumentEvaluation)
