Title: 2016 W Project Problem Description             
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2016 W Project Problem Description            
----

# Project Problem Description
Warning: This is subject to change!

You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the following goals. Your design must be flexible enough to allow developers to extend or migrate it.
We want a mobile application that allows owners to record the things they have and share them with borrowers. For example, a thing could be a good (like a piece of camera equipment), a service (like giving a ride in a car), or a resource (like a parking spot). Generally, a thing should be something reusable and typical underused. It is up to each team to choose some specific thing of focus, with approval from the TA.


In general, a user can be both an owner of their own things and a borrower of someone else's things. A borrower can borrow a thing by making a monetary bid for it. The owner can accept a bid, so the thing becomes borrowed. The owner can denote when a borrowed thing is returned and available again.


## Needs in (Partial) User Story Form
User needs are expressed in the form of partial user stories:
As a <role>, I want <goal>.
These descriptions may change to correct omissions and clarify noticed issues. New requirements will be introduced for the final project part.


### Things
US 01.01.01
As an owner, I want to add a thing in my things, each denoted with a clear, suitable description.
US 01.02.01
As an owner, I want to view a list of all my things, and their descriptions and statuses.
US 01.03.01
As an owner, I want to view one of my things, its description and status.
US 01.04.01
As an owner, I want to edit a thing in my things.
US 01.05.01
As an owner, I want to delete a thing in my things.


### Status
US 02.01.01
As an owner or borrower, I want a thing to have a status of one of: available, bidded, or borrowed.
User profile
US 03.01.01
As a user, I want a profile with a unique username and my contact information.
US 03.02.01
As a user, I want to edit the contact information in my profile.
US 03.03.01
As a user, I want to, when a username is presented for a thing, retrieve and show its contact information.


### Searching
US 04.01.01
As a borrower, I want to specify a set of keywords, and search for all things not currently borrowed whose description contains all the keywords.
US 04.02.01
As a borrower, I want search results to show each thing not currently borrowed with its description, owner username, and status.


### Bidding
US 05.01.01
As a borrower, I want to bid for an available thing, with a monetary rate (in dollars per hour).
US 05.02.01
As a borrower, I want to view a list of things I have bidded on that are pending, each thing with its description, owner username, and my bid.
US 05.03.01
As an owner, I want to be notified of a bid.
US 05.04.01
As an owner, I want to view a list of my things with bids.
US 05.05.01
As an owner, I want to view the bids on one of my things.
US 05.06.01
As an owner, I want to accept a bid on one of my things, setting its status to borrowed. (Any other bids are declined.)
US 05.07.01
As an owner, I want to decline a bid on one of my things.


### Borrowing
US 06.01.01
As a borrower, I want to view a list of things I am borrowing, each thing with its description and owner username.
US 06.02.01
As an owner, I want to view a list of my things being borrowed, each thing with its description and borrower username.


### Returning
US 07.01.01
As an owner, I want to set a borrowed thing to be available when it is returned.


### Offline behavior
US 08.01.01
As an owner, I want to define new things while offline, and push the additions once I get connectivity.


### Photographs
US 09.01.01 (added 2016-02-29)
As an owner, I want to optionally attach a photograph to a thing of mine.

US 09.02.01 (added 2016-02-29)
As an owner, I want to delete any attached photograph for a thing of mine.

US 09.03.01 (added 2016-02-29)
As an owner or borrower, I want to view any attached photograph for a thing.

US 09.04.01 (added 2016-02-29)
As a sys admin, I want each photograph to be under 65536 bytes in size.

### Location
US 10.01.01 (added 2016-02-29)
As an owner, I want to specify a geo location on a map of where to receive a thing when I accept a bid on the thing.

US 10.02.01 (added 2016-02-29)
As a borrower, I want to view the geo location of where to receive a thing I will be borrowing.


### "Wow"
Non-trivial requirement(s) on approval from your TA (added 2016-03-11)