Title: Project Problem Description
date: 2025-08-26
tags: projects, teams, grading
authors: Abram Hindle, Samuel Iwuchukwu, Hazel Victoria Campbell
status: published
summary: Project Problem Description
[TOC]

# Project Problem Description

Warning: This is subject to change!

## **Event Lottery System Application**

You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the following goals. Your design must be flexible enough to allow developers to extend or migrate it.

## **Description:**

We want a mobile application where people can sign up for events at community centres that are popular and fill up fast. We want to allow people with limitations such as work, disability, etc. to be able to sign up for these events fairly and not have to sit refreshing a webpage until they can get a chance at reserving a spot.

How? Lottery! If I am running swimming lessons for 20 kids, I will post my event or series of events and I will let everyone join the waiting list for a period of a week. After the week is up, I will ask the system to choose 20 kids to sign up. The system will then notify these kids (or their guardians), if they say no they don’t want swimming lessons, then the system will sample another child to sign up. I can monitor the progress and then get access to the final list of everyone who signs up. If perhaps someone cancels later I can cancel them in the app and a new applicant is drawn.

Lottery systems are great because you don’t have to be first to get a chance to go to an event, you just have to say you are interested and if you’re lucky you will be offered a chance. This gives people who need the time, the time to sign up properly without a time pressure. Accessibility!


## **Features:**

1. Pooling System:

    + Organizers can draw from a waiting list of interested event attendees as selected participants.

2. QR Code Scanning:

    + entrants can scan QR promotional code to view details about the event and also join the waiting list

3. Firebase Integration:

    + Utilize Firebase for storing event details, attendee lists, and real-time check-in status updates.

4. Multi-User Interaction:

    + Distinguish between entrants, organizers, and admin with special roles and privileges granted to each actor.

5. Image Upload:

    + Allow event organizers upload event poster image

6. Geolocation Verification

    + Have the option to attach a geolocation requirement to verify where users are joining the waiting list from. This is the location provided by the device.

**Scenario:**

1. I want to sign my partner up to swim lessons, they need to learn how to swim if they are going to go canoeing with me. I go to the local rec centre, I see they have listed swimming lessons for beginners, I scan the QR code. I see that it is open to register for 2 more days. I click register. 2 days later when it is closed the system samples people, but not me. It notifies me that I wasn’t sampled in the first draw, but there might be a chance if someone declines. Nobody declines. Boo.

2. I am running an interpretive dance class where I teach the safety basics of dance (no eye gouging, that kind of stuff). I tell the app that I have classes every monday From 2025-01-01 to 2025-03-01, and that you need to register by 2024-12-15 and registration opens on 2024-12-01. The price is $60 and I can accommodate 60 people. I click publish and now an event is made where people can join the waiting list and they get this basic information. Also a QR code is generated that will lead them to this page.

3. I want to sign my partner up to piano lessons, they need to learn how to play if they are going to play piano with me. I go to the app, I go to my local rec centre, I see they have listed piano lessons for beginners, I scan the QR code. I see that it is open to register for 2 more days. I click register. 2 days later when it is closed the system samples people, but not me. It notifies me that I was sample.

**Actors:**

+ Entrant: a person who signs up for an event

+ Organizer: the entity that runs the event

+ Administrator: The entity that administers and runs the infrastructure

**Glossary:**

+ QR Code: a scannable code, either a barcode, a QR code, or other code scannable by Zebra crossing libraries or google QR code scanning libraries.

+ Entrant: someone who declares their interest in signing up for an event by joining the waiting list

+ Waiting List: a record of entrants that showed interest in a specific event

+ Sign Up : An action of registering/confirming for an event when successfully selected
    * You can think of this like accepting an invitation.

+ Profile : A screen on the application that holds information about an entrant

+ Choosing: Randomly selecting a number of entrants in the waiting list to be invited to sign up

+ Event: name, description, a time and place, registration start time and end time, optional promotional poster, organizer, entrants, attendees (accepted).

**User Stories:**

User needs are expressed in the form of partial user stories:

As a (role), I want (goal).

These descriptions may change to correct omissions and clarify noticed issues. New requirements will be introduced for the final project part.

**User:**

US 01.01.01 As an entrant, I want to join the waiting list for a specific event

US 01.01.02 As an entrant, I want to leave the waiting list for a specific event 

US 01.01.03 As an entrant, I want to be able to see a list of events that I can join the waiting list for.

US 01.01.04 As an entrant, I want to filter events based on my interests and availability.


US 01.02.01 As an entrant, I want to provide my personal information such as name, email and optional phone number in the app

US 01.02.02 As an entrant I want to update information such as name, email and contact information on my profile

US 01.02.03 As an entrant, I want to have a history of events I have registered for, whether I was selected or not.

US 01.02.04 As an entrant, I want to delete my profile if I no longer wish to use the app.


<!--- US 01.03.01 As an entrant I want to upload a profile picture for a more personalized experience --->

<!--- US 01.03.02 As an entrant I want remove profile picture if need be --->

<!--- US 01.03.03 As an entrant I want my profile picture to be deterministically generated from my profile name if I haven't uploaded a profile image yet. --->

US 01.04.01 As an entrant I want to receive notification when I am chosen to participate from the waiting list (when I "win" the lottery)

US 01.04.02 As an entrant I want to receive notification of when I am not chosen on the app (when I "lose" the lottery)

US 01.04.03 As an entrant I want to opt out of receiving notifications from organizers and admins

US 01.05.01 As an entrant I want another chance to be chosen from the waiting list if a selected user declines an invitation to sign up.

US 01.05.02 As an entrant I want to be able to accept the invitation to register/sign up when chosen to participate in an event.

US 01.05.03 As an entrant I want to be able to decline an invitation when chosen to participate in an event.

US 01.05.04 As an entrant, I want to know how many total entrants are on the waiting list for an event.

US 01.05.05 As an entrant, I want to be informed about the criteria or guidelines for the lottery selection process.


US 01.06.01 As an entrant I want to view event details within the app by scanning the promotional QR code.

US 01.06.02 As an entrant I want to be able to be sign up for an event by from the event details.

US 01.07.01 As an entrant, I want to be identified by my device, so that I don't have to use a username and password.

<!--- US 01.08.01 As an entrant, I want to be warned before joining a waiting list that requires geolocation. --->

**Organizer:**

US 02.01.01 As an organizer I want to create a new event and generate a unique promotional QR code that links to the event description and event poster in the app.

<!--- US 02.01.02 As an organizer I want to store the generated QR code in my database --->

<!--- US 02.01.03 As an organizer, I want to create and manage my facility profile. --->

US 02.01.04 As an organizer, I want to set a registration period.

US 02.02.01 As an organizer I want to view the list of entrants who joined my event waiting list

US 02.02.02 As an organizer I want to see on a map where entrants joined my event waiting list from.

US 02.02.03 As an organizer I want to enable or disable the geolocation requirement for my event.

US 02.03.01 As an organizer I want to OPTIONALLY limit the number of entrants who can join my waiting list.

US 02.04.01 As an organizer I want to upload an event poster to the event details page to provide visual information to entrants.

US 02.04.02 As an organizer I want to update an event poster to provide visual information to entrants.

US 02.05.01 As an organizer I want to send a notification to chosen entrants to sign up for events.

* This is the notification that they "won" the lottery.

US 02.05.02 As an organizer I want to set the system to sample a specified number of attendees to register for the event.

US 02.05.03 As an organizer I want to be able to draw a replacement applicant from the pooling system when a previously selected applicant cancels or rejects the invitation.

US 02.06.01 As an organizer I want to view a list of all chosen entrants who are invited to apply.

US 02.06.02 As an organizer I want to see a list of all the cancelled entrants.

US 02.06.03 As an organizer I want to see a final list of entrants who enrolled for the event.

US 02.06.04 As an organizer I want to cancel entrants that did not sign up for the event 

US 02.06.05 As an organizer I want to export a final list of entrants who enrolled for the event in CSV format.

US 02.07.01 As an organizer I want to send notifications to all entrants on the waiting list

US 02.07.02 As an organizer I want to send notifications to all selected entrants

US 02.07.03 As an organizer I want to send a notification to all cancelled entrants


**Admin:**

US 03.01.01 As an administrator, I want to be able to remove events.

US 03.02.01 As an administrator, I want to be able to remove profiles.

US 03.03.01 As an administrator, I want to be able to remove images.

<!--- US 03.03.02 As an administrator, I want to be able to remove hashed QR code data --->

US 03.04.01 As an administrator, I want to be able to browse events.

US 03.05.01 As an administrator, I want to be able to browse profiles.

US 03.06.01 As an administrator, I want to be able to browse images that are uploaded so I can remove them if necessary.

US 03.07.01 As an administrator I want to remove organizers that violate app policy.

US 03.08.01 As an administrator, I want to review logs of all notifications sent to entrants by organizers.


**WOW Factor:**

As a bonus 2% to your overall course grade, project teams are able to complete a “wow factor” that differentiates their project from other teams. 
This is an optional component and you can still receive 100% in the course even if you do not complete this. 
Some sample ideas of additions to the project are provided below. 
If you have a different idea than one of the suggestions below then you must approve it with your mentor TA first before working on the feature.

1. Calendar view 
    - Be able to view a calendar of all events, and all registered events based on the device’s time zone.
2. Commenting system
    - Be able to comment on an event
    - Can reply to a comment and make comment threads
    - React to a comment
3. Map of all nearby events that an entrant can join the draw pool for
    - The map events can be filtered out by the event tags
    - There should be some grouping strategies based on the zoom distance of the map
4. Carousel on the main screen to view events
    - Can add other UI components as well
5. Entrant profiles that keeps track of preferences
    - Catered view of the events the entrant can see based on their stored preferences
6. Accessibility mode
    - Color blind mode
    - Larger font, larger buttons, etc.
7. Messaging system
    - Real time messaging system where entrants can ask questions or communicate to organizers via direct messages
8. Confirmation ticket
    - After the pool is draw, generate a confirmation ticket that entrants can download as a PDF







