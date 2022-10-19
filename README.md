# Favour Local Library
A Local Library based on [Mozilla Developer Network Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django).
This web application creates an online catalog for a small local library, where users can browse available books and manage their accounts.

### Features

There are models for books, book instances, genres, languages and authors.
There are 3 posssible users
* Library users
* Libaraians
* Admin

The library users can view details of books and authors and the books they have borrowed.

The libarians can;
* Renew the return date of borrowed books
* Add new authors
* Add new books
* Add new books instance (which include borrowing books to library users)
* Delete books, authors and book instance
* View all borrowed books and users who borrowed them.

The admin can do all what the librarian can do and much more, which include add new users to the library.

### Image view of page for libarians
#### Home page
![Home page image](https://user-images.githubusercontent.com/70489864/196820550-996b65a3-f907-4bd6-95fd-a188eeb3f8c2.png)

#### Book list page
![Book list page image](https://user-images.githubusercontent.com/70489864/196820787-1392df56-1d09-4021-a9c0-79edf500a916.png)

#### Detail of a book
![Detail of a book image](https://user-images.githubusercontent.com/70489864/196820945-04d96166-869e-4c5c-8743-d323990f3275.png)

#### Author list page
![Author list page image](https://user-images.githubusercontent.com/70489864/196821134-de4f31e7-4fa7-4b15-ba21-253c183e3bda.png)

#### Detail of an author
![Detail of an author image](https://user-images.githubusercontent.com/70489864/196821208-2c5f4b47-af64-46c7-a8e4-fb1876a6a3f0.png)

#### Deleting a book
![Deleting a book image](https://user-images.githubusercontent.com/70489864/196821490-5c915d55-d587-4c53-a35d-96709891b106.png)
All book instance of a book would have to be deleted before a book can ba deleted.

#### Access
You can use the credential below to explore what library users can do.
* Username: optimistic
* Password: lovepeaceunity
