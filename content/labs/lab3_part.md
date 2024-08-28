Title: Lab 3 Participation Exercise
date: 2024-01-06
tags: labs, policy, grading
authors: Samuel Iwuchukwu,Hazel Victoria Campbell
status: published
summary: Lab 3 Participation Exercise

[TOC]

# Lab 3 Participation Exercise

Due: Friday, 26 January 2024, 4:00 PM
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

You should submit your exercise solution as a zip or tar archive.