Title: Lab 1 Instructions
date: 2024-08-19
tags: labs, policy, grading
authors: Samuel Iwuchukwu, Hazel Victoria Campbell
status: published
summary: Lab Instructions

----

[TOC]

# Lab 1 -- Java, OOP, Android Studio

**Lab 1 Instructions**

Download and install Android Studio from the official Android website

https://developer.android.com/studio

Check for specific installation guide unique to your Operating System

**https://developer.android.com/studio/install**

Follow the following instructions

**############# LAB Demo #####################**

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

```java
ImportantTweet(String message){
        super(message);
    }
```
+ Super calls the parent's constructor (there is a hidden call to Object's constructor)
+ Change the Tweet to an ImportantTweet in LonelyTwitterActivity

4. Abstract Stuff

+ Make Tweet Class Abstract

    + public abstract class Tweet { ... }
    + public abstract Boolean isImportant();
+ What if they need to behave differently? @Override isImportant() to create a compile-time check

+ Make a NormalTweet class, could have many types of tweets

    + call super in both of  NormalTweet's constructors
    + isImportant method should return Boolean.FALSE
+ What if we want to use both in our list? (Implicit upcasting)

ArrayList<Tweet> tweetList = new ArrayList<Tweet>();
tweetList.add(normalTweet);

+ Abstract method and base class so all the classes have the isImportant() method

+ An interface can also be used to force the use of some methods

```java
public interface Tweetable {
     public String getMessage();
     public Date getDate();
   }
```
+ Make Tweet implement Tweetable


