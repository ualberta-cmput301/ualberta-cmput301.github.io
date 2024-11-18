Title: CMPUT 301 Course Old Project Problem Descriptions Fall 2024
date: 2024-11-12
tags: labs, policy, grading
authors: Samuel Iwuchukwu, Hazel Victoria Campbell
status: published

**Warning: This is subject to change!**

# QR Code Event Check-In System

You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the following goals. Your design must be flexible enough to allow developers to extend or migrate it.

# Description: 

Create an event management system where attendees check in using QR codes on their mobile devices. Organizers can track attendance, manage event details, and send notifications.

# Features:

- QR Code Scanning:

Attendees can use the app to scan event-specific QR codes for quick and seamless check-ins.

- Firebase Integration:

Utilize Firebase for storing event details, attendee lists, and real-time check-in status updates.

- Multi-User Interaction:

Distinguish between organizers and attendees with different app roles and permissions.

- Geolocation Verification (Optional):

Optionally use geolocation to verify that attendees are physically present at the event location during check-in.

- Image Upload:

Allow organizers to upload event posters and attendees to upload profile pictures for a more personalized experience.

# Scenario:
Update for Project 3:

John, an event organizer, opens the QRCheckIn app for an upcoming tech conference. He generates a unique QR code for the event. Potential attendees browse the events and notice John's event, they view the event poster, and then click sign up to indicate they will attend the event as an attendee. As attendees arrive, they use the app to scan the QR code, automatically checking them into the conference. The app updates John's dashboard in real-time, showing the current attendance. John can also send push notifications to all attendees through the app.

Scenario for Project 2:
 John, an event organizer, opens the QRCheckIn app for an upcoming tech conference. He generates a unique QR code for the event. As attendees arrive, they use the app to scan the QR code, automatically checking them into the conference. The app updates John's dashboard in real-time, showing the current attendance. John can also send push notifications to all attendees through the app.

 # Actors:

Organizer: a person who organizes the event and is in control of an event

Attendee: a person who attends the event

Administrator: the entity that is responsible for the infrastructure that the game runs on.

# Glossary:

QR Code: a scannable code, either a barcode, a QR code, or other code scannable by Zebra crossing libraries or google QR code scanning libraries.

# User Stories:

User needs are expressed in the form of partial user stories:

As a <role>, I want <goal>.

These descriptions may change to correct omissions and clarify noticed issues. New requirements will be introduced for the final project part.

# Organizer:

US 01.01.01 As an organizer, I want to create a new event and generate a unique QR code for attendee check-ins.

US 01.01.02 As an organizer, I want the option to reuse an existing QR code for attendee check-ins.

US 01.02.01 As an organizer, I want to view the list of attendees who have checked in to my event.

US 01.03.01 As an organizer, I want to send notifications to all attendees through the app.

US 01.04.01 As an organizer, I want to upload an event poster to provide visual information to attendees.

US 01.05.01 As an organizer, I want to track real-time attendance and receive alerts for important milestones.

US 01.06.01 As an organizer, I want to share a generator QR code image to other apps so I can email or update other documents with the QR code.

US 01.07.01 As an organizer, I want to create a new event and generate a unique promotion QR code that links to the event description and event poster in the app.

US 01.08.01 As an organizer, I want to see on a map where users are checking in from.

US 01.09.01 As an organizer, I want to see how many times an attendee has checked into an event.

[New for Part 3] US 01.10.01 As an organizer, I want to see who is signed up to attend my event.

[New for Part 3] US 01.11.01 As an organizer, I want to OPTIONALLY limit the number of attendees that can sign up for an event.

# Attendee:

US 02.01.01 As an attendee, I want to quickly check into an event by scanning the provided QR code.

US 02.02.01 As an attendee, I want to upload a profile picture for a more personalized experience.

US 02.02.02 As an attendee, I want to remove profile pictures if need be.

US 02.02.03 As an attendee, I want to update information such as name, homepage, and contact information on my profile.

US 02.03.01 As an attendee, I want to receive push notifications with important updates from the event organizers.

US 02.04.01 As an attendee, I want to view event details and announcements within the app.

US 02.05.01 As an attendee, I want my profile picture to be deterministically generated from my profile name if I haven't uploaded an profile image yet.

US 02.06.01 As an attendee, I do not want to login to the app. No username, no password.

[New for Part 3] US 02.07.01 As an attendee, I want to sign up to attend an event from the event details (as in I promise to go).

[New for Part 3] US 02.08.01 As an attendee, I want to browse event posters/event details of other events.

[New for Part 3] US 02.09.01 As an attendee, I want to know what events I signed up for currently and in and in the future.


# Both:

US 03.02.01 As a user, I want the option to enable or disable geolocation tracking for event verification.

# Administrator:

US 04.01.01 As an administrator, I want to be able to remove events.

US 04.02.01 As an administrator, I want to be able to remove profiles.

US 04.03.01 As an administrator, I want to be able to remove images.

US 04.04.01 As an administrator, I want to be able to browse events.

US 04.05.01 As an administrator, I want to be able to browse profiles.

US 04.06.01 As an administrator, I want to be able to browse images.


[New for Part 3 stories do not need to be addressed in Part 2]