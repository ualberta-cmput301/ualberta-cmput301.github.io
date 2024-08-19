Title: Labs
date: 2024-01-06
tags: labs, policy, grading
authors: Hazel Victoria Campbell
status: published
summary: Lab Procedure, Lab Assignments, Lab Marking

----

[TOC]

# Lab Things Go Here

# Lab 1 -- Java, OOP, Android Studio

**Lab 1 Instructions**

Download and install Android Studio from the official Android website

https://developer.android.com/studio

Check for specific installation guide unique to your Operating System

**https://developer.android.com/studio/install**

Follow the following instructions

############# LAB Demo #####################

1. Create a new LonelyTwitter project. Make sure that the project language is Java, not Kotlin!

+ Create Tweet Class (Click > New > Java Class)
+ Make attributes (Date date & String message) (use alt+enter to include)
    + Note: Access modifiers
        * private= class only
        * No modifier = within package
        * protected = through inheritance
        * public = everyone!
+ Create two Constructors (one with the only Message and the other with Date+Message as arguments) and use Date = new Date() (current date and time) for the first constructor (the Default value for date).
+ Note: Java Object Class (everything extends it, calls its constructor and it has built-in methods like toString())
+ Note: the this keyword (message = message doesn't do anything!)
+ Make a regular tweet in LonelyTwitterActivity (pass in an empty string)

2. Getters and setters

3. Inheritance

+ Make ImportantTweet child class (extends Tweet)
    + call super in both of ImportantTweet's constructors
+ Now have access to the parent's methods and attributes. except constructors! (try and make an important Tweet)

