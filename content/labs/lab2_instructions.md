Title: Lab 2 Instructions
date: 2026-06-30
tags: labs, policy, grading
authors: Raj Prasad, Michelle Deng
status: published
summary: Lab 2 Instructions

----

[TOC]

# Lab 2 Instructions

In Lab 2, we'll be doing the following: 

- Quick review of [OOP principles]({attach}slides/2026-Lab-2-OOP-Principles.pdf)
- Android Basics ([Lab 2 Android Basics PDF under Lab 2]({attach}slides/2026-Lab-2-Android-Basics.pdf))
- Displaying a list of items using Jetpack Compose 'LazyColumn' ([Lab 2 Demo Example - Instructions PDF under Lab 2]({attach}slides/2026-Lab-2-ListyCity-Instructions.pdf))
- Lab Exercise - adding and removing items from the city list (see the Lab 2 Participation Exercise below for more details.)


# Lab 2 Participation Exercise

Task: Modify/expand ListyCity to allow for the addition of new cities as well as the deletion of existing ones from the city list. The specifics of the design of this functionality are up to you.

**If you could not attend the labs or do not have the code for ListyCity, follow the instructions in Lab 2 Example - Instructions.** 

Hints:

1. You may want to use the `onClick` callbacks of Compose components such as `Button`, as demonstrated in the lab.

2. Consider how the city list is stored and modified. The `CityRepository` from the lab provides controlled functions for modifying the Compose city list.

3. Ideally, you should consider treating cities as objects, however, in this exercise it may not be necessary.

Here are some screenshots from an example application that demonstrate the required functionality. 

**Your app does not need to look exactly like this demo！！！**

1. Press "ADD CITY" then type the name and press "CONFIRM". This adds a new city name to the list  

2. Tap a city name to select it  then press "DELETE CITY" to remove the city from the list.


![Screen1]({attach}../images/lab2/img1_lab2_main.jpeg){ width=300 style="margin: 20px;"}
![Screen2]({attach}../images/lab2/img2_lab2.png){ width=300 style="margin: 20px;" }
![Screen3]({attach}../images/lab2/img3_lab2.png){ width=300 style="margin: 20px;"}
![Screen4]({attach}../images/lab2/img4_lab2.jpeg){ width=300 style="margin: 20px;" }



# Submission

Canvas

**Note: Proper completion of this exercise is considered as part of course participation.**

**Due Date**

Friday after the Thursday lab at 5 PM
