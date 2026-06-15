from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404, HttpResponseNotAllowed
from django.template import loader
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    template = loader.get_template("books/index.html")
    return HttpResponse(template.render({"books": books}, request))
def show(request, id):
    book = Book.objects.get(id=id)
    if book is None:
        raise Http404("Book is not found")
    return render(request, 'books/show.html', {"book": book})
    # return HttpResponse("show a book with id: %s" % id)

def edit(request, id):
    book = Book.objects.get(id=id)
    if book is None:
        raise Http404("Book not found")

    # Populate the form with the current book's data
    # form = BookForm(initial={
    #     'title': book['title'],
    #     'desc': book['desc'],
    #     'rate': book['rate'],
    #     'views': book['views']
    # })
    form = BookForm(instance=book)
    return render(request, 'books/edit.html', {'form': form, 'book': book})

def update(request, id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    book = Book.objects.get(id=id)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        # Call your custom update classmethod
        form.save()
        return redirect('books_index') # Redirect back to your list view

    # If validation fails, re-render the edit page with errors
    book = Book.one(id)
    return render(request, 'books/edit.html', {'form': form, 'book': book})

def new(request):
    form = BookForm()
    return render(request, 'books/new.html', {"form": form})
    # return HttpResponse("heloo world ")

def create(request):
    if request.method != 'POST':
            return HttpResponseNotAllowed(['POST']) # Guard against accidental GET requests
    form = BookForm(request.POST)
    if form.is_valid():
        book = Book(
            title=form.cleaned_data['title'],
            desc=form.cleaned_data['desc'],
            rate=float(form.cleaned_data['rate']),
            views=int(form.cleaned_data['views'])
        )
        book.save()
        return redirect('books_index') # Redirect to your list view after saving
    
    # If the form has errors, re-render the 'new' template with the error messages
    return render(request, 'books/new.html', {'form': form})
def delete(request, id):
    Book.destroy(id)
    return redirect('books_index')
     