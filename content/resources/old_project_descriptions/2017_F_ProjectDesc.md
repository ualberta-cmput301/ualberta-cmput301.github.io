Title: 2017 F Project Problem Description             
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2017 F Project Problem Description          
----

# Project Problem Description
You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the follow goals. Your design must be flexible enough to allow developers to extend or migrate it.
To assist in forming good habits, we want a mobile application that allows one to track, encourage, and share their habits. Recurring habits could be, for example, "write a joke", "eat breakfast", "exercise dog", "call family", and "no car accident". The intent is to make such habits: regular (e.g., daily), unbroken (so missed habit events are noted), and shared (so there's public pressure not to miss).

## Needs in (Partial) User Story Form
User needs are expressed in the form of partial user stories:
As a <role>, I want <goal>.
These descriptions may change to correct omissions and clarify noticed issues. Talk to the customer and propose options, rather than making what might be an unwarranted assumption or interpretation.

### Habits
US 01.01.01
As a participant, I want to add a new type of habit, giving it a brief title, reason, and date to start.
US 01.02.01
As a participant, I want a habit to have a plan for what days of the week it should regularly occur.
US 01.03.01
As a participant, I want to view a given habit and its details.
US 01.04.01
As a participant, I want to edit the details of a habit of mine.
US 01.05.01
As a participant, I want to delete a habit of mine.
US 01.06.01
As a participant, I want a habit title to be no more than 20 characters and habit reason to be no more than 30 characters.
US 01.07.01
As a participant, I want to see what habits I need to do today.
US 01.08.01
As a participant, I want for each habit type, a visual and statistical habit status indicator to show how closely I am following its plan.

### Habit Events
US 02.01.01
As a participant, I want to add a habit event to my habit history when I have done a habit as planned.
US 02.02.01
As a participant, I want a habit event to have an optional comment of no more than 20 characters.
US 02.03.01
As a participant, I want a habit event to have an optional photograph to record what happened.
US 02.04.01
As a participant, I want to view a given habit event and all its available details.
US 02.05.01
As a participant, I want to edit the details of a habit event of mine.
US 02.06.01
As a participant, I want to delete a habit event of mine.
US 02.07.01
As a system administrator, I want the storage for each photographic image to be under 65536 bytes.

### Profile
US 03.01.01
As a participant, I want to be uniquely identifiable.
Habit History
US 04.01.01
As a participant, I want to view as a list my habit history, sorted in reverse chronological order (most recent coming first).
US 04.02.01
As a participant, I want to filter my habit history list to show only a particular type of habit.
US 04.03.01
As a participant, I want to filter my habit history list to show only habit events whose comment text contains a given word.

### Habit Following and Sharing
US 05.01.01
As a participant, I want to ask another participant to follow the statuses of all their habits, and follow for each of their habits, its most recent event.
US 05.02.01
As a participant, I want to grant another participant permission to follow the statuses of all my habits, and follow for each of my habits, its most recent event.
US 05.03.01
As a participant, I want to view as a list the habit statuses of the participants I am granted to follow, ordered by participant identifier then habit title.
Geolocation and Maps
US 06.01.01
As a participant, I want to optionally attach my current location to a habit event.
US 06.02.01
As a participant, I want to see a map of the habit events (that have locations) from my filtered habit history list.
US 06.03.01
As a participant, I want to see a map of the recent habit events (that have locations) from participants I am following.
US 06.04.01
As a participant, I want to highlight habit events of mine or by participants I am following that are within 5 km of my current location.

### Offline Behavior
US 07.01.01
As a participant, I want to add, edit, or delete a habit event while offline, and have any of these changes synchronized once I get connectivity.

### "Wow" Factor
Non-trivial requirement(s) of your choice that fit with the app, on approval from your TA
An example could be collecting kudos or badges from other participants. Another example could be partnering for certain habits, like "play tennis".