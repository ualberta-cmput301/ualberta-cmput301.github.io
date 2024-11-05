Title: 2020 W Project Problem Description          
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2020 W Project Problem Description      
----

**Warning: This is subject to change!**

## You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the following goals. Your design must be flexible enough to allow developers to extend or migrate it.
We want a mobile application that allows drivers to search for open and recent ride requests, and for riders to post requests for rides. Riders will describe the start and end of their ride and their suggested payment. Drivers will browse for nearby requests and accept ride requests that they are willing to fulfil. We're going to use the new baloney currency QR-Bucks! It's like an IOU but in QR code form!

## Needs in (Partial) User Story Form
User needs are expressed in the form of partial user stories:
**As a <role>, I want <goal>.**
These descriptions may change to correct omissions and clarify noticed issues. New requirements will be introduced for the final project part.
### Requests
US 01.01.01
As a rider, I want to request rides between two locations.
US 01.02.01
As a rider, I want to see current request I have open.
US 01.03.01
As a rider, I want to be notified if my request is accepted.
US 01.04.01
As a rider, I want to cancel requests.
US 01.05.01
As a rider, I want to be able to phone or email the driver who accepted a request.
US 01.06.01
As a rider, I want an estimate of a fair fare to offer to drivers and I should be able to offer more.
US 01.07.01
As a rider, I want to confirm the completion of a request and enable payment.

US 01.08.01
As a rider, I want to cancel a ride before the rider picks me up.
US 1.10.01
As a rider, I want to see the driver's profile and ratings.

US 1.11.01
As a rider, I want to rate a driver for his/her service thumbs up or thumbs down.

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

### Searching
US 04.01.01
As a driver, I want to browse and search for open requests by geo-location.

### Accepting
US 05.01.01
As a driver,  I want to accept a request I agree with and accept that offered payment upon completion.
US 05.02.01
As a driver, I want to view the current active request.
US 05.03.01
As a driver, I want to be notified if my ride offer was accepted.

### Offline behavior
US 06.01.01
As an driver, I want to see requests that I already accepted while offline.
US 06.02.01
As a rider, I want to see the current request, even if I am offline.

### Location
US 07.01.01
As a rider, I want to specify a start and end geo locations on a map for a request.
US 07.02.01
As a driver, I want to view start and end geo locations on a map for a request.

### Payment
US 08.01.01
As a rider I wish to generate a QR-Bucks QR Code for my driver to scan to pay them.
US 08.02.01
As a driver I want to scan my rider's QR-Bucks to get paid!

<br>

Note: QR-Bucks do not exist yet, please enable the generation and scanning of QR-Bucks for payment. It can be dummy values like "Abram owes me $10.00"