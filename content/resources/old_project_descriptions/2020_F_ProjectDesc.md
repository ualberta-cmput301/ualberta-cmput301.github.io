Title: 2020 F Project Problem Description        
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2020 F Project Problem Description    
----

Warning: This is subject to change!

You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the following goals. Your design must be flexible enough to allow developers to extend or migrate it.

We want a mobile application that allows owners to record the books they have and loan them to borrowers.

In general, a user can be both an owner of their own books and a borrower of someone else's books. A borrower can borrow an available book by making a request for it. The owner can accept such a request. When the book is handed over, the book becomes borrowed. The owner can denote when a borrowed book is returned and available again.

Needs in (Partial) User Story Form

User needs are expressed in the form of partial user stories:

As a <role>, I want <goal>.

These descriptions may change to correct omissions and clarify noticed issues. New requirements will be introduced for the final project part.

### Books

US 01.01.01
As an owner, I want to add a book in my books, each denoted with a clear, suitable description (at least title, author, and ISBN).

US 01.02.01
As an owner, I want the book description by scanning it off the book (at least the ISBN).

US 01.03.01
As an owner or borrower, I want a book to have a status to be one of: available, requested, accepted, or borrowed.

US 01.04.01
As an owner, I want to view a list of all my books, and their descriptions, statuses, and current borrowers.

US 01.05.01
As an owner, I want to view a list of all my books, filtered by status.

US 01.06.01
As an owner, I want to view and edit a book description in my books.

US 01.07.01
As an owner, I want to delete a book in my books.

### User profile

US 02.01.01
As an owner or borrower, I want a profile with a unique username and my contact information.

US 02.02.01
As an owner or borrower, I want to edit the contact information in my profile.

US 02.03.01
As an owner or borrower, I want to retrieve and show the profile of a presented username.

### Searching

US 03.01.01
As a borrower, I want to specify a keyword, and search for all books that are not currently accepted or borrowed whose description contains the keyword.

US 03.02.01
As a borrower, I want search results to show each book with its description, owner username, and status.

### Requesting

US 04.01.01
As a borrower, I want to request a book that is not currently accepted or borrowed.

US 04.02.01
As a borrower, I want to view a list of books I have requested, each book with its description, owner username, and status.

US 04.03.01
As an owner, I want to be notified of a request.

US 04.04.01
As an owner, I want to view all the requests on one of my books.

### Accepting

US 05.01.01
As an owner, I want to accept a request on one of my books. (Any other requests on the book are declined.)

US 05.02.01
As an owner, I want to decline a request on one of my books.

US 05.03.01
As a borrower, I want to be notified of an accepted request.

US 05.04.01
As a borrower, I want to view a list of books I have requested that are accepted, each book with its description, and owner username.

### Borrowing

US 06.01.01
As an owner, I want to hand over a book by scanning the book ISBN code and denoting the book as borrowed.

US 06.02.01
As a borrower, I want to receive an accepted book by scanning the book ISBN code to confirm I have borrowed it.

US 06.03.01
As a borrower, I want to view a list of books I am borrowing, each book with its description and owner username. 

### Returning

US 07.01.01
As a borrower, I want to hand over a book I borrowed by scanning the book ISBN code to denote the book as available.

US 07.02.01
As an owner, I want to receive a returned book by scanning the book ISBN code to confirm I have it available.

### Photographs

US 08.01.01
As an owner, I want to optionally attach a photograph to a book of mine.

US 08.02.01
As an owner, I want to delete any attached photograph for a book of mine.

US 08.03.01
As an owner or borrower, I want to view any attached photograph for a book.

### Location

US 09.01.01
As an owner, I want to specify a geo location on a map of where to receive a book when I accept a request on the book.

US 09.02.01
As a borrower, I want to view the geo location of where to receive a book I will be borrowing.