Title: Assignment 0: Getting Started
date: 2024-08-12
tags: individual, policy, grading
authors: Hazel Victoria Campbell, Ken Wong, Abram Hindle
status: published
summary: Assignment 0: Getting Started
----

[TOC]

* **Due date:** Check the [schedule]({filename}/pages/home.md#schedule).

# Learning Objectives

* Learn how to use Android Studio on your computer.
* Learn to create, build, and run a simple Android app.

# Problem Description

Install Android Studio on your own computer.

Make and run a simple hello world app according to the Build your first app in this [tutorial:](https://web.archive.org/web/20240324083233/https://developer.android.com/codelabs/build-your-first-android-app?hl=en#0). Ensure you do all of this tutorial, including the final section on Fragments.

In Step 6.10 where it says type in 0 into your TextView type in your student number instead. So the count button will increment your student number. Do not prefix your student number with zeros. 6.10 is section 10 [of this link](https://web.archive.org/web/20240324083233/https://developer.android.com/codelabs/build-your-first-android-app?hl=en#0)
Deliverables
Screenshots:

    First screenshot: Take a first screenshot of your running app before you press the count button, it should show your student number.

    Second screenshot: Take a second screenshot of your running app showing the activity after you tap the Count button 7 times. The result should be your student number + 7

    Each screenshot should not show the development environment, just the device display with the user interface of the running app. Capturing the frame of the emulator window is fine.

# Submission Procedure

Use a non-lossy image format for the screenshots (like PNG with usually lossless settings, and not JPEG with usually lossy settings).

Do not use a phone camera to take the images.

Name the two screenshot files with your CCID (e.g., kennyw-1.png, kennyw-2.png). Zip the files (e.g., kennyw.zip) and upload the archive using eClass.

The maximum upload size is 5 MB.

Proper completion of this assignment is considered as part of course participation.

Upload your zip file to eClass under "Assignment 0".

# Hints

IF you have build.gradle.ktx files, for the last step instead of

```
def nav_version = "2.3.0-alpha04"
classpath "androidx.navigation:navigation-safe-args-gradle-plugin:$nav_version"
```

in your `build.gradle.ktx` (Project: My Frist App), You need

```
buildscript {
    repositories {
        google()
    }
    dependencies {
        val nav_version = "2.7.6"
        classpath("androidx.navigation:navigation-safe-args-gradle-plugin:$nav_version")
    }
}
```

And instead of:

```
apply plugin: 'androidx.navigation.safeargs'
```

You need in your build.gradle.ktx (module: app):

```
plugins {
    id("androidx.navigation.safeargs")
}
```

There is also an error step 8 of task 9 that if you get an error about an unresolved inport

```
"import androidx.navigation.fragment.navArgs" 
```

but you can just remove that import its not needed for Java code.
