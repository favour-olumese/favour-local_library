from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

# ------------------------------
# Defining a class for BookInstance to be edited inline in Book details
# Using TabularInline. You could also check StackedInline
class BooksInstanceInline(admin.TabularInline):
        model = BookInstance
        extra = 0  # This is removes the default extra 3 empty instances

# ------------------------------
# Creating and registering an admin class for Book
#admin.site.register(Book)

# Define the book admin class
class BookAdmin(admin.ModelAdmin):
        
        # Using list display to display info. of books.
        list_display = ('title', 'author', 'display_genre')

        # Adding inline edditing of BookInstance in Book detail page.
        inlines = [BooksInstanceInline]
      
# Register the admin class with the associated model
admin.site.register(Book, BookAdmin)


# ------------------------------
# Defining a class for Books items to be displayed inline in Author detail view
class BookInline(admin.StackedInline):
        model = Book
        extra = 0  # Remove the default extra 3 empty slots.

# ------------------------------
# Creating and registering an admin class for Author
# admin.site.register(Author)

# Define the author admin class
class AuthorAdmin(admin.ModelAdmin):
        
        # Using list display to display info. of authors.
        list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

        # Make the DOB and DOD be on the same line.
        fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
        
        # Adding Books to be displayed in Author datail view.
        inlines = [BookInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# ------------------------------
# Creating and registering an admin class for BookInstance
# admin.site.register(BookInstance)

# Registering the Admin classes for the BookInstance using the decorator
@admin.register(BookInstance)

# Define the bookinstance admin class
class BookInstanceAdmin(admin.ModelAdmin):
        list_display = ('book', 'status', 'due_back', 'id')
        list_filter = ('status', 'due_back')

        # Seperate the data form into two group of fields.
        # The first has no title, while the other has the title, 'Availability.'
        fieldsets = (
                (None, {
                        'fields': ('book', 'imprint', 'id')
                }),
                ('Availabilty', {
                        'fields': ('status', 'due_back')
                }),
        )


# ------------------------------
# This is the simplest way of registering a model, or models, with the site.
admin.site.register(Genre)
admin.site.register(Language)
