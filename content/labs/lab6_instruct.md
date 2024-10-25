Title: Lab 6 Instructions
date: 2024-08-26
tags: labs, policy, grading
authors: Samuel Iwuchukwu,Hazel Victoria Campbell
status: published
summary: Lab 6 Instructions
[TOC]

# Lab 6 Instructions

1. Follow the slides on [Javadoc]({attach}slides/Javadoc.pdf) and [JUnit]({attach}slides/JUnit.pdf)

2. Follow instructions on this [link]({attach}slides/Lab_6_Instructions_F24_updated.pdf) along with the TA.

3. Complete Lab Exercise.  



## Some known issues:

1. "test events were not received" --> Solution: [link](https://stackoverflow.com/a/73009440/1496554)

2. "Error creating JavaDoc" --> Solution: [link](https://stackoverflow.com/a/73102343/1496554)


# Lab 6 Participation Exercise

Proper completion of this exercise is considered as part of course participation.

In this exercise your task is to **implement and test** the following methods in the CityList class **AND create Javadocs** for the main source files (not tests):

1) Implement and test these methods:
    - hasCity(City city)
        - When given a city, return whether or not it belongs in the list

        - Test to see whether your method is correct (Read https://www.infoworld.com/article/3305792/comparing-java-objects-with-equals-and-hashcode.html) delete(City city)

        - Check if a city is present in the list. If it does then remove it from the list, if not then **throw an exception**

        - Test to see if your method actually removes it from the list

        - Test to see if the exception is actually thrown (Read more here https://howtodoinjava.com/junit5/expected-exception-example/) countCities()

        - Return how many cities are in the list

        -  Test to see whether your method is correct
        
2) Add Javadocs to all methods in CityList class and City class **AND** generate the javadocs to <project-name>/app/javadocs

Submit the whole Project folder (not just source files or 'app')directory

**Due Date**

Friday after the Thursday lab at 4PM