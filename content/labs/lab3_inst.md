Title: Lab 3 Instructions
date: 2024-01-06
tags: labs, policy, grading
authors: Samuel Iwuchukwu,Hazel Victoria Campbell
status: published
summary: Lab 3 Instructions

[TOC]

# Lab 3 Instructions - What we'll do in lab!

In Lab 3, together we'll go through the following:


1. Going through Lab 3 Slides PDF  ([customize ArrayAdapter and Fragments]({attach}slides/Lab_3_Slides_Winter_2023.pdf))
2. Supporting a ListView with items that have multiple views using a custom ArrayAdapter and Using a Fragment to add new cities to ListyCity ([customize ArrayAdapter and Fragments code & walkthrough]({attach}slides/Lab_3_Instructions_Winter_2023.pdf))

Download the Starter code [here]({attach}slides/ListyCityLab3.zip)

Read about Java code conventions (see the [Code Conventions (Schoepp) PDF]({attach}slides/Code_Conventions_Schoepp.pdf)).

Editing existing cities in ListyCity (see the Lab 3 Participation Exercise below for more details)

# Lab 3 Participation Exercise

Note: Proper completion of this exercise is considered as part of course participation.

Task: Add functionality to ListyCity to allow editing an existing city. The specifics of the design of this functionality are up to you.

If you could not attend the labs or do not have the code for the updated Lab 3 ListyCity, follow Lab 3 Instructions for ListyCity CustomList and then ListyCity Fragment. You can also download the "Lab 3 Demo" code from eClass.

**Your app does not need to look exactly like the screenshots. All that is required is the ability to edit an existing city. You can implement it and make it look like however you want.**

![Screen1]({attach}../images/lab3/img1_lab3.png){width=300 style="margin: 20px;"}
![Screen2]({attach}../images/lab3/img2_lab3.png){width=300 style="margin: 20px;"}
![Screen3]({attach}../images/lab3/img3_lab3.png){width=300 style="margin: 20px;"}
![Screen4]({attach}../images/lab3/img4_lab3.png){width=300 style="margin: 20px;"}


Hints:
1. **Add setters** to your City class so that you can modify its name and province.

2. You may need to **pass the City object that is clicked in the Activity into the Fragment.** One way to do this is to **make a constructor for the Fragment that takes in a City,** and **store the City in the Fragment as an instance variable.** If you do this, make sure to also add an empty constructor to the Fragment so you can use it when adding a new City.
Another way you can send a City object from the Activity to the Fragment is by adding a **"newInstance" method in the Fragment,** and use this method to create a new Fragment when editing a City. In this method, you **take in a City and store it in the Fragment's Bundle object** (if you do this, **make sure that your City class implements the "Serializable" interface, so that it can be saved into the Bundle**). Later on in your onCreateDialog method, you can **access the Bundle using getArguments() and retrieve the City object there.** Note that storing data in a Bundle is similar to storing data in an Intent using key-value pairs. (This is the preferred way to do it in Android, because you usually should not have custom constructors for your Fragments. See here for more info).

Example of a newInstance method in AddCityFragment (Hint #3) 

![Screen5]({attach}../images/lab3/img5_lab3.png){width=300 style="margin: 20px;"}

# Submission

GitHub Classroom

**Due Date**

Friday after the lab at 4PM
