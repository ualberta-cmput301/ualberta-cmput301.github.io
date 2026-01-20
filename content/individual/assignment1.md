Title: Assignment 1
date: 2025-09-02
tags: individual, policy, grading
authors: Hazel Victoria Campbell, Ken Wong, Abram Hindle
status: published
summary: Assignment 1
----

[TOC]

* **Due date:** Check the [schedule]({filename}/pages/home.md#schedule).

### Assignment: EmotiLog - A Quick Emotion Logging App

# **Learning Objectives:**

-   Create a simple, interactive mobile application using Android and
    Java.
-   Document an object-oriented design using Unified Modeling Language
    (UML).

# **Problem Description:**

Develop an Android app called **YOURCCID-EmotiLog** (e.g.,
kennyw-EmotiLog) that allows users to quickly log their feelings or
significant events by pressing emoticon buttons. The app should enable
users to easily record each selected emoticon along with the
corresponding timestamp, and then provide a summary of logs by frequency
over a specified period.

1.  Features:

    -   **Preset Emoticon Buttons:** 6 to 9 customizable emoticon
        buttons representing different feelings or events (e.g., Happy,
        Sad, Grateful, Angry, Excited, etc.).
    -   **Logging Functionality:** Each button press records the
        selected emoticon and the current timestamp.
    -   **Daily Summary:** Users can view a summary of logged emoticons
        for each day, including total counts and frequencies.
    -   **User-Friendly Interface:** The app must provide a simple and
        attractive user interface to enhance ease of use.
    -   **Note:** Your app does not need to have a database with database persistence. Session persistence is fine.

2.  Deliverables:

    1.  **Code Base:**
        -   Complete Android Studio project and compiled APK.
        -   Each class must be properly commented to describe its
            purpose, design rationale, and any outstanding issues.
    2.  **Video:**
        -   A demonstration video (max 3 minutes) showing the app\'s
            core functionalities without audio. It should illustrate how
            to log emoticons and view summaries.
    3.  **System Documentation:**
        -   UML class diagram(s) detailing the app\'s object-oriented
            design. Include notes on each class\'s main
            responsibilities.

3.  Demonstration Actions:

    1.  Open the app from the launcher.
    2.  Show the main screen with emoticon buttons.
    3.  Press an emoticon button (e.g., Happy)
    4.  Navigate to the list of emoticon events and confirm that it logs
        the selected emoticons with the timestamp.
    5.  Return to main screen with emoticon buttons.
    6.  Press 1 emotion 10 times in rapid succession.
    7.  Navigate to the list of emoticon events and confirm that it logs
        the selected emoticons with the timestamp.
    8.  Return to the main screen.
    9.  Press 1 emotion 5 times in rapid succession.
    10. Go to the summary screen and show the emoticon counts.

4.  Hints

    This is a description of the core functionality. Often, problem
    statements from users lack details. As you are prototyping a design,
    you may uncover other behaviors that have not been specified, but
    make sense in the context and intent of the application. For
    example, think about how someone might effectively use your
    application. It is up to you to decide what functions your design
    will need, based on the given problem description and valid
    assumptions, in discussion with your users (the TAs and instructor).
    You should consider asking the customer (the instructor) what they
    want to see. While you may discuss your design with other students,
    the code and documentation must be your own work.

    Code from publicly available sources may be used within reason and
    only if their licenses permit so. Always fully cite to give proper
    credit to the original developers in the source code and in the
    system documentation. For example, in citing a work, at least state:
    from whom, the date of publication, license, and URL. Do what is
    required by its license.

    The TAs will be inspecting your code, so \"major\" commented-out
    experiments should be cleaned up so that the code is readable.

    Do not skimp on the UML class diagrams in the system documentation.
    For neatness and readability, diagrams should be created or drawn
    using a vector graphics editing tool and exported in a common,
    non-lossy graphics format.

    Besides addressing the problem correctly, your software design will
    be evaluated on its proper use of object-oriented design concepts,
    such as separation of concerns and information hiding.

5.  Losing Marks

    You may lose marks for any of the following:

    -   **files not in properly named subdirectories**
    -   missing compiled binary APK file for the app
    -   cannot run the app after install
    -   cannot distinguish CCID from the app name
    -   cannot view files without specialized tools
    -   lossy compression used in image file(s) for UML (e.g., JPEG)
    -   inadequate or improper citations
    -   using RAR archive format

    These are brown M&M rules.

6.  Submission Procedure:

    -   Create a directory named **YOURCCID-EmotiLog** (e.g.,
        kennyw-EmotiLog) and include the following subdirectories:
        **code**, **video**, **doc**.
    -   Place the Android Studio project in the **code** directory.
    -   Include the APK file under
        **code/app/build/outputs/apk/debug/app-debug.apk**.
    -   Store the demonstration video in the **video** directory.
    -   Keep UML documentation in the **doc** directory.
    -   Zip the **YOURCCID-EmotiLog** directory and upload.
    -   **NOTE:** If any of the above submission steps are not followed then the misplaced file(s) will be considered "incomplete" and your grade reduced accordingly.

7.  Evaluation Criteria:

    The submission will be assessed according to the following
    categories:

    -   **Excellent (8):** Functionality meets all requirements,
        intuitive UI, comprehensive UML, and a clear video
        demonstration.
    -   **Good (7):** Minor issues but overall functional and follows
        submission rules.
    -   **Satisfactory (5):** Runs, but noticeable issues; some
        requirements may be missing; UML is present but may be
        incomplete.
    -   **Unsatisfactory (4):** Significant issues affecting
        functionality or missing requirements.
    -   **Failure (0):** Incomplete submissions or missing vital
        components such as Videos, UML, or code.

    Excellent (8):

    -   The app is fully functional, meeting all the specified
        requirements.
    -   The user interface is intuitive, attractive, and responsive.
    -   The app follows the brown M&M rules.
    -   The UML documentation is comprehensive and accurately represents
        the object-oriented design.
    -   The video demonstration clearly showcases all required actions,
        and the app performs flawlessly in the demo.
    -   Must have a Video
    -   Must have UML
    -   Must Have Codebase

    Good (7):

    -   The app runs and performs the expected functionalities.
    -   Minor issues may be present, such as a small bug or a slight
        deviation from the requirements.
    -   The user interface is satisfactory but may have some room for
        improvement.
    -   The app follows the brown M&M rules.
    -   The UML documentation is mostly complete but may have minor
        omissions.
    -   Must have a Video
    -   Must have UML
    -   Must Have Codebase

    Satisfactory (5):

    -   The app runs, but there are noticeable issues affecting its
        stability or functionality.
    -   Some requirements may be missing or not fully implemented.
    -   The user interface is functional but may lack polish or suffer
        from usability issues.
    -   The app may not fully adhere to the brown M&M rules.
    -   The UML documentation is present but may be incomplete or
        inaccurate.
    -   Must have a Video
    -   Must have UML
    -   Must Have Codebase

    Unsatisfactory (4):

    -   Effort has been put into the assignment, but the app may not run
        well or may have significant functionality issues.
    -   Several requirements are missing or not implemented.
    -   The user interface may be confusing or challenging to use.
    -   The app may not follow the brown M&M rules.
    -   The UML documentation lacks essential components, incomplete,
        inaccuate.
    -   Must have a Video
    -   Must have UML
    -   Must Have Codebase

    Failure (0):

    -   The assignment is incomplete, lacking essential components such
        as UML documentation, video demonstration, or code.
    -   No submission is provided.
    -   Could be missing any one of these: Video, UML, Codebase

