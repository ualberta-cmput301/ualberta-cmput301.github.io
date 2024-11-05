Title: 2021 W Project Problem Description        
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2021 W Project Problem Description    
----

Warning: This is subject to change!

You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the following goals. Your design must be flexible enough to allow developers to extend or migrate it.

We want a mobile application that allows crowd-sourced testing of phenomona. There are 4 kinds of crowd-sourced tests: counts (how many did you see), binomial trials (pass fail), non-negative integer counts (each trial has 0 or more), measurement trials (like the temperature).

Count-based tests are about how many of something a person observed, it could be blue cars. Everytime they see a blue car they add 1 to the count seen. For instance you want to crowdsource how many blue cars are seen in Edmonton.

Binomial trials are trials where there's a chance to pass or fail. Users will repeat these trials and indicate pass or success. It could be a series of trials where you try to flip a water bottle upside down.

Non-negative integer counts are trials where each trial results in a non-negative integer results (usually a count). Such as if I drop a carton of eggs, how many eggs survive.

Measurement trials are repeated measurements and you record a decimal value of whatever was measured.

A chief experimenter (owner) describes and proposes a trial, gives rules and constraints that crowd experimenters will follow when they execute the trials. The crowd experimenters will look for trials that interest them, subscribe to trials and help execute and record trials for these experiments.

Needs in (Partial) User Story Form

User needs are expressed in the form of partial user stories:

As a <role>, I want <goal>.

These descriptions may change to correct omissions and clarify noticed issues. New requirements will be introduced for the final project part.

### Experiment

US 01.01.01
As an owner, I want to publish an experiment with a description, a region, and a minimum number of trials.

US 01.02.01
As an owner, I want to unpublish an experiment.

US 01.03.01
As an owner, I want to end an experiment. This leaves the results available and public but does not allow new results to be added.

US 01.04.01
As an owner or experimenter, I want to subscribe to an experiment to participate in it.

US 01.05.01
As an experimenter, I want to be able to execute trials for an experiment and upload them to the experiment.

US 01.08.01
As an owner, I want to ignore certain experimenters results.

US 01.09.01
As an owner or experimenter, I want to observe statistics (quartiles, median, mean, stdev) about a current trials.

US 01.06.01
As an owner or experimenter, I want to see histograms of the results of trials.

US 01.07.01
As an owner or experimenter, I want to see plots of the results of trials over time.

<br>

### Questions

US 02.01.01
As an experimenter, I want to ask a question about an experiment.

US 02.02.01
As an experimenter or owner, I want to ask to reply to questions about an experiment.

US 02.03.01
As an experimenter or owner, I want to browse questions and replies about an experiment.

QR Codes

US 03.01.01
As an experimenter, I want to be able to generate QR codes that I can print for a specific experiment and trial result (for instance PASS for a binomial trial I subscribed to).

US 03.02.01
As an experimenter, I want to be able scan QR codes to indicate success or failure, or increment counts for trials I subscribed to.

US 03.03.01
As an experimenter, I want to be able to register an arbitrary bar code (such as one off of your favourite book) to act a specific experiment result for a trial.

<br>

### User profile

US 04.01.01
As an owner or experimenter, I want a profile with a unique username and my contact information.

US 04.02.01
As an owner or experimenter, I want to edit the contact information in my profile.

US 04.03.01
As an owner or experimenter, I want to retrieve and show the profile of a presented username.

US 04.04.01 *new for Part 4*

As an owner or experimenter, I do not want to log into my application using a username and password.

<br>

### Searching

US 05.01.01
As an experimenter, I want to specify a keyword, and search for all experiments that are available.

US 05.02.01
As an experimenter, I want search results to show each experiment with its description, owner username, and status.

<br>

### Location

US 06.01.01
As an owner, I want to specify a Geo-location is required or not for trials.

US 06.02.01
As an experimenter, I want to add Geo-location to experimental trials that need it.

US 06.03.01
As an experimenter, I want to be warned about geo-location trials.

US 06.04.01
As an experimenter, I want to see a map of geo-locations of a geo-location enabled expirement.