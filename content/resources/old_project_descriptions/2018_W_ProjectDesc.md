Title: 2018 W Project Problem Description               
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2018 W Project Problem Description            
----

# Project Problem Description
Warning: This is subject to change!

You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the following goals. Your design must be flexible enough to allow developers to extend or migrate it.

We want a mobile application that allows task requesters to post the tasks they would like done by task providers. For example, a task could be giving a ride in a car or delivering a package, within the city.

In general, a user of the app could be both a task requester and a task provider. A task provider can offer their service by making a monetary bid on a task. The task requester can accept a bid, so the task is assigned to the winning task provider. The task requester can denote when the task is done.

## Needs in (Partial) User Story Form

User needs are expressed in the form of partial user stories:

As a <role>, I want <goal>.

These descriptions may change to correct omissions and clarify noticed issues.

### Task Basics

US 01.01.01
As a task requester, I want to add a task to my tasks, each denoted with a title, brief description, and initial status: requested.

US 01.01.02 (added 2018-02-14)
As a task requester, I want the maximum length of the task title to be at least 30 characters.

US 01.01.03 (added 2018-02-14)
As a task requester, I want the maximum length of the task description to be at least 300 characters.

US 01.02.01
As a task requester, I want to view a list of my tasks, with their titles and statuses.

US 01.03.01 (revised 2018-02-16)
As a task requester, I want to edit the details for any one of my tasks with status: requested.

US 01.04.01
As a task requester, I want to delete a task of mine.

### Task Details

US 02.01.01
As a task requester or provider, I want to view all the details for a given task, including its title, description, status, and lowest bid so far (if any).

US 02.02.01
As a task requester or provider, I want a task to have a status to be one of: requested, bidded, assigned, or done.

Bidded means at least one provider bidded on the task.

### User Profile

US 03.01.01
As a user, I want a profile with a unique username and my contact information.

US 03.01.02 (added 2018-02-16)
As a user, I want the maximum length of a username to be at least 8 characters.

US 03.01.03 (added 2018-02-16)
As a user, I want the contact information to include an email address and a phone number.

US 03.02.01
As a user, I want to edit the contact information in my profile.

US 03.03.01
As a user, I want to, whenever a username is shown, be able to retrieve and see its corresponding contact information.

### Searching

US 04.01.01
As a task provider, I want to specify a set of keywords, and search for all tasks, with status: requested or bidded, whose description contains all the keywords.

US 04.02.01
As a task provider, I want search results to show each task with its task requester username, title, status, lowest bid so far (if any).

### Task Bidding

US 05.01.01
As a task provider, I want to make a bid on a given task with status: requested or bidded, using a monetary amount.

US 05.02.01 (revised 2018-02-14)
As a task provider, I want to view a list of tasks that I have bidded on, each with its task requester username, title, status, lowest bid so far, and my bid.

US 05.03.01
As a task requester, I want to be notified of a bid on my tasks.

US 05.04.01
As a task requester, I want to view a list of my tasks with status bidded, each having one or more bids.

US 05.05.01
As a task requester, I want to view the bids on one of my tasks.

US 05.06.01 (revised 2018-03-28)
As a task requester, I want to accept a bid on one of my tasks, setting its status to assigned, and declining any other bids on that task.

US 05.07.01 (revised 2018-03-28)
As a task requester, I want to decline a bid on one of my tasks.

Declining may be done by marking the bid as such or hiding it.

### Task Assigned

US 06.01.01
As a task provider, I want to view a list of tasks I am assigned, each task with its task requester username, title, status, and my accepted bid.

US 06.02.01
As a task requester, I want to view a list of my tasks with status: assigned, each task with its task provider username, title, status, and accepted bid.

### Task Done

US 07.01.01
As a task requester, I want to set a task with status: assigned to have status: done, when it is completed.

US 07.02.01 (revised 2018-03-28)
As a task requester, I want to set a task with status: assigned to have status: requested, when it is not completed and there are no other bids on it.

US 07.03.01 (added 2018-03-28)
As a task requester, I want to set a task with status: assigned to have status: bidded, when it is not completed and there are other bids on it.

### Offline behavior

US 08.01.01
As a task requester, I want to add or edit tasks while off the network, and have these changes synchronized once I regain connectivity.

### Photographs

US 09.01.01
As a task requester, I want to optionally attach one or more photographs as further viewable details to a task of mine.

US 09.01.02 (added 2018-04-06)
As a task requester, I want the maximum number of photographs that can be attached to a task to be at least 10.

US 09.02.01
As a task requester or provider, I want to view any attached photograph for a task.

US 09.03.01
As a sys admin, I want each photograph to be under 65536 bytes in size.

### Geolocation and Maps

US 10.01.01
As a task requester, I want to specify a geo location on a map as further viewable details to a task of mine.

US 10.02.01
As a task requester or provider, I want to view any geo location for a task, on a map.

US 10.03.01
As a task provider, I want to see a map of all tasks (that have locations), with status: requested or bidded, that are within 5 km of my current location.

### "Wow" Factor

Non-trivial, visible requirement(s) of your choice that fit with the app, on approval from your TA. This should be decided for the initial use cases.

An example could be a way to rate task providers and see their ratings. Another could be dealing with tasks (that have locations) from a map view.