# documents/views.py
from django.shortcuts import redirect, render, get_object_or_404
from .models import Document, DocumentEvaluation
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm, DocumentEvaluationForm

def document_list(request):
    documents = Document.objects.all()  # Fetch all documents
    return render(request, 'documents/document_list.html', {'documents': documents})


def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk)
    evaluations = DocumentEvaluation.objects.filter(document=document)
    if request.method == 'POST':
        form = DocumentEvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.document = document
            evaluation.user = request.user
            evaluation.save()
    else:
        form = DocumentEvaluationForm()
    return render(request, 'documents/document_detail.html', {'document': document, 'evaluations': evaluations, 'form': form})

@login_required
def add_document(request):
    # Handle form submission
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)  # Handle file upload
        if form.is_valid():
            form.save()  # Save the document to the database
            return redirect('document_list')  # Redirect to document list page after successful addition
    else:
        form = DocumentForm()  # Create an empty form if it's a GET request

    return render(request, 'documents/add_document.html', {'form': form})
def home(request):
    return render(request, 'documents/add.html')
