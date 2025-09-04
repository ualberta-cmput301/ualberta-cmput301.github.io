Title: Lab 1
date: 2024-08-19
tags: labs, policy, grading
authors: Samuel Iwuchukwu, Hazel Victoria Campbell
status: published
summary: Lab 1 -- Java, OOP, Android Studio

----

[TOC]

# Lab 1 Slides

* [Lab 1 Slides]({attach}slides/CMPUT_301_LAB_1.pdf)

# Instructions

Download and install Android Studio from the official Android website

<https://developer.android.com/studio>

Check for specific installation guide unique to your Operating System

<https://developer.android.com/studio/install>

## Walkthrough

1. Create a new LonelyTwitter project (File > New > New Project > Select "Empty Views Activity"). Make sure that the project language is **Java**, not Kotlin!

+ Create Tweet Class (Click > New > Java Class)
+ Make attributes (Date date & String message) (use alt+enter (windows) or Option-Enter (Mac) to include/import any packages)
    + Note: Access modifiers
        * private= class only
        * No modifier = within package
        * protected = within package and through inheritance
        * public = everyone!
+ Create two Constructors (one with the only Message and the other with Date+Message as arguments) and use Date = new Date() (current date and time) for the first constructor (the Default value for date).
+ Note: Java Object Class (everything extends it, calls its constructor and it has built-in methods like toString())
+ Note: the this keyword (message = message doesn't do anything!)
+ Make a regular tweet in MainActivity (pass in an empty string)

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
+ Change the Tweet to an ImportantTweet in MainActivity

4. Abstract Stuff

+ Make Tweet Class Abstract

    + public abstract class Tweet { ... }
        + Note: Abstract classes cannot be instantiated.
    + public abstract Boolean isImportant();
        + This is an abstract method, it has no implementation and must be overridden by child classes (to add functionality).
        + Note: Abstract methods cannot be called using any objects.

+ What if they need to behave differently? @Override isImportant() to create a compile-time check
    + You need to override the method in the child class as it is an abstract method in the parent class that has no implementation.
    + Overriding the method allows the child class to have its own implementation of the method.
        + ex. the Normal Tweet is not important, so it returns false. The ImportantTweet is important, so it returns true.
    + The methods in the child classes need to be overridden to behave differently.

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



# Lab1 Participation Exercise Requirements

1. Add three new model classes to LonelyTwitter: the first should be an abstract base class which represents the current mood. The second and third should be non-abstract classes which represent different moods (Ex: happy, sad, etc.) and inherit from the abstract class.
2. Each mood should have a date and getters and setters to access the date.
3. A constructor which sets the date to a default and a constructor which takes a date as an argument should be provided. 
4. Encapsulation should be followed.
5. Each mood should have a method which returns a string representing that mood.
6. Your new code should have examples of classes, methods, attributes, access modifiers, encapsulation, constructors, inheritance and abstract base classes.

# Submission

GitHub Classroom

Note: Running the project is not necessary.


* **Due date:** Check the [schedule]({filename}/pages/home.md#schedule). (Usually Friday after the lab at 4PM)
