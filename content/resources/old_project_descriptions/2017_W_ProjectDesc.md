Title: 2017 W Project Problem Description             
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2017 W Project Problem Description            
----

# Project Problem Description
You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the follow goals. Your design must be flexible enough to allow developers to extend or migrate it.
To assist in understanding the emotional states and triggers of individuals and groups, we want a mobile application that allows one to post, track, and share their moods. For  university students or staff, this could allow a clearer picture of their experiences, perceptions, and mental well-being in the face of challenges in academic life.

## Needs in (Partial) User Story Form
User needs are expressed in the form of partial user stories:
As a <role>, I want <goal>.
These descriptions may change to correct omissions and clarify noticed issues. Talk to the customer and propose options, rather than making what might be an unwarranted assumption or interpretation.

### Moods
US 01.01.01
As a participant, I want to add a mood event to my mood history, each event with the current date and time, a required emotional state, optional trigger, and optional social situation.
US 01.02.01
As a participant, I want the emotional states to include at least: anger, confusion, disgust, fear, happiness, sadness, shame, and surprise.
US 01.03.01
As a participant, I want consistent emoticons and colors to depict and distinguish the emotional states in any view.
US 01.04.01
As a participant, I want to view a given mood event and all its available details.
US 01.05.01
As a participant, I want to edit the details of a given mood event of mine.
US 01.06.01
As a participant, I want to delete a given mood event of mine.

### Other Details
US 02.01.01
As a participant, I want to express the reason why for a mood event using a brief textual explanation (no more than 20 characters or 3 words).
US 02.02.01
As a participant, I want to express the reason why for a mood event using a photograph.
US 02.03.01
As a system administrator, I want the storage for each photographic image to be under 65536 bytes.
US 02.04.01
As a participant, I want to specify the social situation for a mood event to be one of: alone, with one other person, with two to several people, or with a crowd.

### Profile
US 03.01.01
As a user, I want a profile with a unique username.

### Mood History
US 04.01.01
As a participant, I want to view as a list my mood history, sorted by date and time, in reverse chronological order (most recent coming first).
US 04.02.01
As a participant, I want to filter my mood history list to show only mood events that occurred in the most recent week.
US 04.03.01
As a participant, I want to filter my mood history list to show only mood events with a particular emotional state.
US 04.04.01
As a participant, I want to filter my mood history list to show only mood events whose reason why text contains a given word.

### Mood Following and Sharing
US 05.01.01
As a participant, I want to ask another participant to follow their most recent mood event.
US 05.02.01
As a participant, I want to grant another participant permission to follow my most recent mood event.
US 05.03.01
As a participant, I want to view as a list the most recent mood events of the participants I am granted to follow, sorted by date and time, in reverse chronological order (most recent coming first).
US 05.04.01
As a participant, I want to filter my mood following list to show only mood events that occurred in the most recent week.
US 05.05.01
As a participant, I want to filter my mood following list to show only mood events with a particular emotional state.
US 05.06.01
As a participant, I want to filter my mood following list to show only mood events whose reason why text contains a given word.

### Geolocation and Maps
US 06.01.01
As a participant, I want to optionally attach my current location to a mood event.
US 06.02.01
As a participant, I want to see a map of the mood events (showing their emotional states) from my filtered mood history list (that have locations).
US 06.03.01
As a participant, I want to see a map of the mood events (showing their emotional states and the username) from my filtered mood following list (that have locations).
US 06.04.01
As a participant, I want to see a map of the most recent mood event of every participant (showing their emotional states) if the event has a location and is within 5 km of my current location.

### Offline Behavior
US 07.01.01
As a participant, I want to add, edit, or delete a mood event while offline, and have any of these changes synchronized once I get connectivity.

### "Wow" Factor
Non-trivial requirement(s) that fit with the app on approval from your TA