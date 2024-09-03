Title: Assignment 1
date: 2024-08-12
tags: individual, policy, grading
authors: Hazel Victoria Campbell, Ken Wong, Abram Hindle
status: published
summary: Assignment 1
----

[TOC]

* **Due date:** Check the [schedule]({filename}/pages/home.md#schedule).

# **Learning Objectives**
Solve a problem by constructing a simple, interactive application using Android and Java.

Document an object-oriented design in Unified Modeling Language.

# **Problem Description**

Consider the situation of someone who wants to create and manage a wishlist of books they want to read. Develop a simple, attractive, and intuitive Android mobile app to assist users in organizing their reading preferences. Let's name this app: YOURCCID-MyBookWishlist (e.g., kennyw-MyBookWishlist).

Using this app, users can maintain a list of books they wish to read. Each book entry in the wishlist has the following editable fields:

+ Book title (textual, up to 50 characters)
+ Author name (textual, up to 30 characters)
+ Genre (e.g., Fiction, Non-Fiction, Mystery)
+ Publication year (four-digit integer)
+ Status (Read/Unread)

The app must allow the user to:

+ Show a list of books in their wishlist, displaying the title, author, genre, and read status.
+ Add a new book to the wishlist (appends to the bottom of the list).
+ View and edit the details of an existing book entry, including title, author, genre, and read status.
+ Delete a book from the wishlist.
+ See the total number of books in the wishlist and the count of books marked as read.

The list need not display all the information for an item if screen space is limited. Minimally, each item in the list should show its title, author, genre, and read status.

The app must assist the user in proper data entry. For example, use appropriate user interface controls to enforce particular data types and avoid illegal values.

For this assignment, the data need not be persistent across runs of the app.

The app must assist the user in proper data entry. For example, use appropriate user interface controls to enforce particular data types and avoid illegal values.

For this assignment, the data need not be persistent across runs of the app.

Encode your campus computing ID in the app name. Specifically, the app name must show up as YOURCCID-MyBookWishlist (e.g., kennyw-MyBookWishlist).

# **Deliverables**

1. **Code Base:**
Your complete source code and compiled binary, implementing the working app and its user interface, will be inspected and run by the TA. The Android Studio project and APK (Android Package Kit) binary must be included in the submission. Each class must contain comments describing its purpose, design rationale, and any outstanding issues.

2. **Video:**
The video is a demonstration of the app. The video file must be included in the submission. The video is meant to show that the demonstration actions below actually work. No audio is needed. Maximum duration is 3 minutes. Focus on just the screen of the app, not the whole desktop. For visual clarity, do not use a handheld camera.

3. **System Documentation:**
Describe the structure of your app's object-oriented design using UML class diagram(s), saved as non-lossy image file(s). Focus on the most important classes that you designed and implemented. Add notes to describe the main responsibilities of these classes.

# **Demonstration Actions**

1. Open the app from the launcher.

2. Show the list of books in the wishlist, with none so far. (This could be the initial screen.)

3. Add a book to the wishlist with the title "The Great Gatsby," author "F. Scott Fitzgerald," genre "Fiction," publication year 1925, and status "Unread."

4. Show the list and the total count, with this item.

5. View/edit this item to update the title to "The Great Gatsby: Updated Edition" and mark it as "Read."

6. Show the list and the updated counts, with this modified item.

7. Add another book to the wishlist with the title "To Kill a Mockingbird," author "Harper Lee," genre "Fiction," publication year 1960, and status "Unread."

8. Show the list and the updated counts, with the two books.

9. Add one more book to the wishlist with your CCID as the author and your student number as the title of the book, status "Read", year 2024.

10. Show the list and the updated counts, with the three books.

11. View/edit the details of one book in the wishlist.

12. Delete one book from the wishlist.

13. Show the list, with the remaining books.

14. View the details of one book in the wishlist.

15. Delete the remaining books from the wishlist.

# **Hints**
This is a description of the core functionality. Often, problem statements from users lack details. As you are prototyping a design, you may uncover other behaviors that have not been specified, but make sense in the context and intent of the application. For example, think about how someone might effectively use your application. It is up to you to decide what functions your design will need, based on the given problem description and valid assumptions, in discussion with your users (the TAs and instructor). You should consider asking the customer (the instructor) what they want to see.

While you may discuss your design with other students, the code and documentation must be your own work. Code from publicly available sources may be used within reason and only if their licenses permit so. Always fully cite to give proper credit to the original developers in the source code and in the system documentation. For example, in citing a work, at least state: from whom, the date of publication, license, and URL. Do what is required by its license.

The TAs will be inspecting your code, so "major" commented-out experiments should be cleaned up so that the code is readable.

Do not skimp on the UML class diagrams in the system documentation. For neatness and readability, diagrams should be created or drawn using a vector graphics editing tool and exported in a common, non-lossy graphics format.

Besides addressing the problem correctly, your software design will be evaluated on its proper use of object-oriented design concepts, such as separation of concerns and information hiding.

# **Losing Marks**
You may lose marks for any of the following:

files not in properly named subdirectories
missing compiled binary APK file for the app
cannot run the app after install
cannot distinguish CCID from the app name
cannot view files without specialized tools
lossy compression used in image file(s) for UML (e.g., JPEG)
inadequate or improper citations
These are brown M&M rules.

# **Submission Procedure**
Create an assignment directory called YOURCCID-MyBookWishlist (e.g., kennyw-MyBookWishlist), and within it have three subdirectories: code,  video,  doc. 

Your Android Studio project directory goes within code. The compiled binary APK file(s) should be found within an /app/build/intermediates/apk/debug/app-debug.apk subdirectory or /app/build/outputs/apk/debug/app-debug.apk within the project directory. The video file goes in the video subdirectory. The UML documentation goes in the doc subdirectory.

Zip the assignment directory and upload to eClass. 

**e: It must be a zip file with the .zip file extension.**

Please make sure all the required files are included to build the app. The TA will test your app from the submitted code and APK file.

The app name must show up as YOURCCID-MyBookWishlist (e.g., kennyw-MyBookWishlist), so that it can be easily distinguished from other submissions.

**This is how the assignment will be marked:**

There are no inbetween marks, no part marks.


Rubric for Android App Assignment - MyBookWishlist

Excellent (8):

+ The app is fully functional, meeting all the specified requirements.
+ The user interface is intuitive, attractive, and responsive.
+ The app follows the brown M&M rules.
+ The UML documentation is comprehensive and accurately represents the object-oriented design.
+ The video demonstration clearly showcases all required actions, and the app performs flawlessly in the demo.
+ Must have a Video
+ Must have UML
+ Must Have Codebase

Good (7):

+ The app runs and performs the expected functionalities.
+ Minor issues may be present, such as a small bug or a slight deviation from the requirements.
+ The user interface is satisfactory but may have some room for improvement.
+ The app follows the brown M&M rules.
+ The UML documentation is mostly complete but may have minor omissions.
+ Must have a Video
+ Must have UML
+ Must Have Codebase

Satisfactory (5):

+ The app runs, but there are noticeable issues affecting its stability or functionality.
+ Some requirements may be missing or not fully implemented.
+ The user interface is functional but may lack polish or suffer from usability issues.
+ The app may not fully adhere to the brown M&M rules.
+ The UML documentation is present but may be incomplete or inaccurate.
+ Must have a Video
+ Must have UML
+ Must Have Codebase

Unsatisfactory (4):

+ Effort has been put into the assignment, but the app may not run well or may have significant functionality issues.
+ Several requirements are missing or not implemented.
+ The user interface may be confusing or challenging to use.
+ The app may not follow the brown M&M rules.
+ The UML documentation lacks essential components, incomplete, inaccuate.
+ Must have a Video
+ Must have UML
+ Must Have Codebase

Failure (0):

+ The assignment is incomplete, lacking essential components such as UML documentation, video demonstration, or code.
+ No submission is provided.
+ Could be missing any one of these: Video, UML, Codebase
