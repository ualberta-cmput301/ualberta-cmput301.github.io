Title: 2018 F Project Problem Description             
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2018 F Project Problem Description          
----

# Project Problem Description
Warning: This is subject to change!

You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the following goals. Your design must be flexible enough to allow developers to extend or migrate it.

## User's Problem Description
I went to my doctor and had a physical. It was embarassing. The doctor pointed out some spots and asked if I had seen them before. I wasn't sure, so neither put pushed the issue any further. We didn't know, so we weren't going to do anything. Another time I went to the doctor and had the doctor investigate a spot on my hand. The doctor asked me if it had changed, I wasn't sure. The doctor asked me if it had grown, I said I assume so because why am I noticing it now. The doctor shrugged, said it looked alright and told me to keep track of it. Come back if it changed.



I can't remember if it changes, to prove something changed I need evidence. I could take photos of my whole body and keep them in a safe place, but would I remember to take the photos again and consistently? I also would like to take notes as well.



Thus I want software that will run on my phone and allow me to take photos of skin issues and notes about medical issues I might have. These photos and notes will be for my own sanity as well I can provide them to physicians when they are needed.



Each photo or note should be timestamped and associated with a problem. Each photo or note should optionally be mapped to a location. Each photo or note should be associated with a location on my body which I can indicate by clicking on paper-doll-cut-out-like image of myself. So if my left arm was affected, I'd click on my left arm on a picture of myself--that body location would recorded. If I suffer headaches near smokestacks I probably want to record the GPS location as well.



Thus as a user I want to be able to track and document medical issues. I want to use my cellphone to help me document all the blemishes and marks, and other stuff on my body such that I can keep track of them.



## Needs in (Partial) User Story Form

User needs are expressed in the form of partial user stories:

As a <role>, I want <goal>.

These descriptions may change to correct omissions and clarify noticed issues.

### Task Basics

US 01.01.01

As a patient I want to record my problems, each denoted with a title, date started, and a brief description.

US 01.01.02 (added 2018-02-14)
As a patient, I want the maximum length of the task title to be at least 30 characters.

US 01.01.03 (added 2018-02-14)
As a patient, I want the maximum length of the task description to be at least 300 characters.

US 01.02.01
As a patient, I want to view a list of my problems, with their titles, dates, and number of records.

US 01.03.01 (revised 2018-02-16)
As a patient, I want to edit the details for any one of my problems.

US 01.04.01
As a patient, I want to delete a problem of mine.

US 01.05.01

As a patient I want to add records (photos, locations, comments) to problems.

### Record Details

US 02.01.01
As a patient or care provider, I want to view all the records for a given problem, including its title, description, photo, etc.

US 02.02.01
As a patient, I want to add records to problems.

US 02.03.01
As a patient, records can have a geo-location.

US 02.04.01
As a patient, records can have a body location.

US 02.05.01
As a patient, records can have a title and comment.

US 02.06.01
As a patient, records can have a photo.

US 02.07.01
As care provider, I want to add new comment records to a problem for my patients.

US 02.08.01
As a patient, records have a timestamp.

US 02.09.01

As a patient, I want some method of helping me take consistent photos, so that when I show the doctor any progression such as the growth of a mole is evident.


US 02.10.01

As a patient, I need to have a slideshow mode whereby photo records of a problem can be browsed by clicking. So I could "animate” changes to a doctor.

### User Profile

US 03.01.01
As a patient, I want a profile with a unique userid and my contact information.

US 03.01.02
As a patient, I want the minimum userid to be at least 8 characters.

US 03.01.03
As a patient, I want the contact information to include an email address and a phone number.

US 03.02.01
As a patient, I want to edit the contact information in my profile.

US 03.03.01
As a patient or care provider, I want to, whenever a username is shown, be able to retrieve and see its corresponding contact information.


**US 03.04.01 *new***

**As a patient or care provider, I do not want to have to ever use a password, remember a password, or have to care about a password. If I need security tokens or anything like that it must be hidden from me.**

**US 03.05.01 *new**

**As a patient or care provider, when I use a new device I want to be able to use the same profile.**

**US 03.06.01 *new***

**As a patient, I want to be able to share a very short code, or something visually scannable by a photo camera, with a care provider so they can add my profile.**

**US 03.07.01 *new***

**As a patient, I want to be able to share a very short code, or something visually scannable by a photo camera, with myself so I can enable a new device to browse as me.**


### Searching

US 04.01.01
As a patient or care provider, I want to specify a set of keywords, and search for all problems or records that contains all the keywords.

US 04.02.01
As a patient or care provider, I want to specify a set of keywords, and search for all problems or records that are near a particular Geo-location.

US 04.03.01
As a patient or care provider, I want to specify a set of keywords, and search for all problems or records that are near a particular body-location.

### Patient Assigned

US 06.01.01
As a care provider, I want to view a list of patients I am assigned to.

### Care Provider

US 07.01.01

As a care provider, I want to add patients that I am assigned to.

US 07.01.02

As a care provider, I want to want to browse my patients problems.

US 07.01.03

As a care provider, I want to add comment records to my patients' problems

### Offline behavior

US 08.01.01
As a patient, I want to add or edit problems and records while off the network, and have these changes synchronized once I regain connectivity.

### Photographs

US 09.01.01
As a patient, I want to optionally attach one or more photographs as further viewable details to a record of mine.

US 09.01.02 (added 2018-04-06)
As a patient, I want the maximum number of photographs that can be attached to a record to be at least 10.

US 09.02.01
As a patient or care provider, I want to view any attached photograph for a record.

US 09.03.01
As a sys admin, I want each photograph to be under 65536 bytes in size.

### Geolocation and Maps

US 10.01.01
As a patient, I want to specify a geo location on a map of a record.

US 10.02.01
As a patient or provider, I want to view any geo location for a record, on a map.

US 10.03.01
As a patient or care provider, I want to see a map of all records for a patient (that have locations).

### Body-locations

US 11.01.01

As a patient, I want to upload at least front and back body-location photos so I may indicate where photo records were taken on my body.

US 11.02.01

As a patient, body locations are effectively a reference to a body-location photo and a point location on the photo.

US 11.03.01

As a patient, I should be able to have at least 2 body location pictures.

US 11.04.01

As a patient, when I view a body location it should be a clear indicator of a point on a body-location picture.


**US 11.05.01 *new***

**As a patient, when making a record I want to choose from available body locations to associate with a photo or a record.**

**US 11.06.01 *new***

**As a patient, I should be able to add body location photos.**

**US 11.07.01 *new***

**As a patient, I should be able to remove body location photos.**

**US 11.08.01 *new***

**As a patient, I should be able to label body location photos.**

**US 11.09.01 *new***

**As a patient, I want body-location photos stored locally on my device (and remotely) so that access to them is fast.**


### Sys-admin

**US 12.01.01 *new***

**As a sysadmin, I want to use a Free/Libre Open Source Software service-side tool such as Elasticsearch to host this application. No proprietary software for data-hosting.**

### "Wow" Factor
Non-trivial, visible requirement(s) of your choice that fit with the app, on approval from your TA. This should be decided for the initial use cases.

An example could be a nice UI for the paper-cut-out-doll view. Another could be dealing with records (that have locations) from a map view.

Another wow factor could be encryption---if you can encrypt photos that are uploaded.