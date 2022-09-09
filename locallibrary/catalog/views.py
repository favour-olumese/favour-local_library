from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects.
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()

    # Available books (status = 'a').
    num_instance_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_genres = Genre.objects.all().count()

    book_starts_with_t = Book.objects.filter(title__istartswith='T').count()

    context = {
        'num_books': num_books,
        'num_instance': num_instance,
        'num_instance_available': num_instance_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'book_starts_with_t': book_starts_with_t,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)