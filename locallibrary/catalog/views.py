import datetime
from django.shortcuts import render, get_object_or_404
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from catalog.forms import RenewBookForm
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect, Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q


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

    genres = Genre.objects.all()

    # Number of visits to this view, as counted in the session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instance': num_instance,
        'num_instance_available': num_instance_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'book_starts_with_t': book_starts_with_t,
        'num_visits': num_visits,
        'genres': genres,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    # For pagination
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class BorrowedBooksListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan of all users."""
    model = BookInstance
    template_name = 'catalog/all_borrowed_books.html'
    paginate_by = 10
    permission_required = 'catalog.can_mark_returned'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

@login_required
@permission_required('catalog.can_renew', raise_exception=True)
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request, the process and
    # populate it wwith data from the request (binding).
    form = RenewBookForm(request.POST)

    # Check if the form is valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        # (here we just write it to the model due_back field)
        book_instance.due_back = form.cleaned_data['renewal_date']
        book_instance.save()

        # Redirect to a new URL:
        return HttpResponseRedirect(reverse('borrowed-books'))

    # If this is a GET reques
    # (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)

class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'author_image']
    initial = {'date_of_birth': '0999-12-28'}
    permission_required = 'catalog.can_edit_authors'

class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    fields = '__all__'  # Not recommended.
    # (potential security issue if more fields are added).
    permission_required = 'catalog.can_edit_authors'

class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'catalog.can_edit_authors'

class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language', 'book_image']
    permission_required = 'catalog.can_edit_books'

class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language', 'book_image']
    permission_required = 'catalog.can_edit_books'

class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'catalog.can_edit_books'

class BookInstanceCreate(PermissionRequiredMixin, CreateView):
    model = BookInstance
    fields = ['id', 'book', 'imprint', 'due_back', 'borrower', 'status']
    permission_required = 'catalog.can_edit_books'
    success_url = reverse_lazy('books')

# The link to updating a book instance is not on any of the templates
# Because renew_book_librarian updates the needed portion (The date of return)
class BookInstanceUpdate(PermissionRequiredMixin, UpdateView):
    model = BookInstance
    fields = ['id', 'book', 'imprint', 'due_back', 'borrower', 'status']
    permission_required = 'catalog.can_edit_books'
    success_url = reverse_lazy('books')

class BookInstanceDelete(PermissionRequiredMixin, DeleteView):
    model = BookInstance
    permission_required = 'catalog.can_edit_books'

    def get_success_url(self, **kwargs):
        # Get the primary key (id) of the book instance
        # https://stackoverflow.com/a/13528732
        book_instance_id = self.kwargs['pk']

        # Use the book instance primary key to get the book_id referenced
        book_reference_id =  BookInstance.objects.filter(id=book_instance_id).values('book_id')[0]['book_id']

        return reverse_lazy('book-delete', kwargs={'pk': book_reference_id})


class GenreListView(generic.ListView):
    model = Genre
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # To get the primary key from the url request.
        genre_id = self.kwargs['pk']

        # QuerySet of all the books of a particular genre
        context['genre_book_list'] = Genre.objects.filter(pk=genre_id)[0].book_set.all()
        context['num_books'] = Genre.objects.filter(pk=genre_id)[0].book_set.all().count()

        # Getting the name of the genre requested based on the primary key
        context['genre_name'] = str(Genre.objects.filter(pk=genre_id)[0])
        return context

    def get_queryset(self):
        '''This function ensures that a 404 page is displayed when we try to GET a wrong genre page.'''
        self.genre = get_object_or_404(Genre, id=self.kwargs['pk'])
        return Genre.objects.filter(name=self.genre)


def search(request):
    """View for searching for books and authors."""
    search_data = request.GET.get("search")

    # Prevent whitespace and empty search
    if search_data == '' or search_data == ' ':
        query_count = 0

        context = {
            'search_data': search_data,
            'query_count': query_count,
        }

        return render(request, 'catalog/search.html', context)

    # Check if search can be found in Author and Book models
    author_query = Author.objects.filter(Q(first_name__icontains=search_data) | Q(last_name__icontains=search_data))
    book_query = Book.objects.filter(title__icontains=search_data)
    query_count = len(author_query) + len(book_query)

    context = {
        'search_data': search_data,
        'author_query': author_query,
        'book_query': book_query,
        'query_count': query_count,
    }

    return render(request, 'catalog/search.html', context)

def page_not_found(request, exception):
    """View for 404 error."""
    print("404 error")
    print(exception)

    return render(request, '404.html')


def handler500(request, exception=None, *_, **_k):
    """View for status 500 error."""
    print("500 error")
    print(exception)

    return render(request, "500.html")

# I have redirected both the 404 and 500 errors to the 404.html.