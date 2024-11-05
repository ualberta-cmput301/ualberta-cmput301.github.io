Title: 2016 F Project Problem Description             
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2016 F Project Problem Description            
----

# Project Problem Description
**Warning: This is subject to change!**
You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the following goals. Your design must be flexible enough to allow developers to extend or migrate it.
We want a mobile application that allows drivers to search for recent ride requests, and for riders to post requests for rides. Riders will describe the start and end of their ride and their suggested payment. Drivers will browse for nearby requests and accept ride requests that they are willing to fulfil.

In general, a user can be both a driver and a rider.

<br>

## Needs in (Partial) User Story Form
User needs are expressed in the form of partial user stories:
As a <role>, I want <goal>.
These descriptions may change to correct omissions and clarify noticed issues. New requirements will be introduced for the final project part.

### Requests
US 01.01.01
As a rider, I want to request rides between two locations.
US 01.02.01
As a rider, I want to see current requests I have open.
US 01.03.01
As a rider, I want to be notified if my request is accepted.
US 01.04.01
As a rider, I want to cancel requests.
US 01.05.01
As a rider, I want to be able to phone or email the driver who accepted a request.
US 01.06.01
As a rider, I want an estimate of a fair fare to offer to drivers.
US 01.07.01
As a rider, I want to confirm the completion of a request and enable payment.
US 01.08.01
As a rider, I want to confirm a driver's acceptance. This allows us to choose from a list of acceptances if more than 1 driver accepts simultaneously.

US 1.09.01 (added 2016-11-14)
As a rider, I should see a description of the driver's vehicle.

US 1.10.01 (added 2016-11-14)
As a rider, I want to see some summary rating of the drivers who accepted my offers.

US 1.11.01 (added 2016-11-14)
As a rider, I want to rate a driver for his/her service (1-5).


### Status
US 02.01.01
As a rider or driver, I want to see the status of a request that I am involved in
User profile
US 03.01.01
As a user, I want a profile with a unique username and my contact information.
US 03.02.01
As a user, I want to edit the contact information in my profile.
US 03.03.01
As a user, I want to, when a username is presented for a thing, retrieve and show its contact information.

US 03.04.01 (added 2016-11-14)
As a driver, in my profile I can provide details about the vehicle I drive.

### Searching
US 04.01.01
As a driver, I want to browse and search for open requests by geo-location.
US 04.02.01
As a driver, I want to browse and search for open requests by keyword.

US 04.03.01 (added 2016-11-14)
As a driver, I should be able filter request searches by price per KM and price.

US 04.04.01 (added 2016-11-14)
As a driver, I should be able to see the addresses of the requests.

US 04.05.01 (added 2016-11-14)
As a driver, I should be able to search by address or nearby an address.

### Accepting
US 05.01.01
As a driver,  I want to accept a request I agree with and accept that offered payment upon completion.
US 05.02.01
As a driver, I want to view a list of things I have accepted that are pending, each request with its description, and locations.
US 05.03.01
As a driver, I want to see if my acceptance was accepted.
US 05.04.01
As a driver, I want to be notified if my ride offer was accepted.

### Offline behavior
US 08.01.01
As an driver, I want to see requests that I already accepted while offline.
US 08.02.01
As a rider, I want to see requests that I have made while offline.
US 08.03.01
As a rider, I want to make requests that will be sent once I get connectivity again.
US 08.04.01
As a driver, I want to accept requests that will be sent once I get connectivity again.

### Location
US 10.01.01
As a rider, I want to specify a start and end geo locations on a map for a request.
US 10.02.01
As a driver, I want to view start and end geo locations on a map for a request.


**Requirements cluster 1:**
US 1.09.01 (car details)
US 03.04.01 (car details)
US 04.03.01 (price search)
US 1.10.01 (ratings)
US 1.11.01 (ratings)


**Requirements cluster 2:**
US 1.09.01 (car details)
US 03.04.01 (car details)
US 04.03.01 (price search)
US 04.04.01 (addresses)
US 04.05.01 (addresses)