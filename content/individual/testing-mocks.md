Title: Individual Assignment 2: Testing with Mocks
date: 2024-01-30
tags: labs, policy, grading
authors: Hazel Victoria Campbell, Sarah Nadi
status: published
summary: Individual Assignment 2: Testing with Mocks
----

[TOC]

# Overview

Most parts of software systems do not work in isolation and are difficult to test when the environment changes. Rather, these parts collaborate with multiple components to perform tasks that we want to implement and test. Various forms of mocks, stubs, fakes and other objects are used in many forms of testing to simulate the behavior of real objects that our implementation depends on to perform a specific task. One of the benefits of mocking dependencies is that we can focus on testing our implementation given that we have obtained the information that we expected from those dependencies. Furthermore, it allows to simulate error conditions in the environment and thus to test a system for robustness. In this assignment, you will test a desktop application by mocking a network service.

# Learning Goals

* Apply mocking testing tools and techniques.
* Overcome mocking difficulties caused by conflicting tools.
* Unit test functionalities of a desktop application that depends on a network service
* Design test cases to assess robustness of error handling implementations

# Resources

* Github API [https://github-api.kohsuke.org/](https://github-api.kohsuke.org/)
* Mockito API [https://site.mockito.org/](https://site.mockito.org/)
* EasyMock API [http://easymock.org/](http://easymock.org/)
* Create your repository by accessing [the GitHub classroom assignment](https://classroom.github.com/a/P6dDMwhK)


# Task: Unit test functionalities of a desktop application

You are developing a GitHub dataminer in Java. Your application will automate a few data gathering tasks on GitHub that may be of interest, such as finding out what day of the week (Monday, Tuesday, etc.) someone makes the most commits on. The current code is really basic and you are allowed to extend it. When developing your miner, you realize that interacting with the GitHub API is not simple as you expected. You need to obtain a token for interacting with the API. Also you do not want to run into API limits due to your tests running too often. You want to test whether your application could handle network connections gracefully. Primarily, you want to test the logic of your application and your error handling mechanisms, assuming you have already interacted with GitHub and received some response from the API. **Your goal in this assignment is to mock the [Java GitHub API](https://github-api.kohsuke.org/) dependency to test your implementation and its robustness.**

The starter code contains some basic functionality for a GitHub miner. Extend the miner as described below and automate testing of the functionality of your miner without actually interacting with the real GitHub API. **In the process, you may need to modify the existing source code to make the project testable (e.g., private methods cannot be tested and static method calls cannot be mocked).**

## Step 1: Interesting Information

The application must determine the following information:

1. What day of the week you make the most git commits on.
2. What is the average time between commits
3. How long do issues on your repos stay open for, on average (consider only closed issues)
4. How long do pull requests on your repos stay open for, on average
5. How many branches do your repos have, on average

There is some code provided to help you get started with #1, but you should improve the code.
#2-5 don't exist in the code at all yet. You need to add the functionality yourself.

Test each of these functionalities without actually communicating with the GitHub servers.
Your code should only communicate with the GitHub servers if Main is run normally, outside of tests. You do not need to test the Main function of the miner, just the functions that abstract the above mining functionality.

## Step 2: Robustness Tactic

In addition to the above functionally, you need to improve the error handling mechanism of the application. Instead of the application crashing with some error if a task could not be completed, you need to retry 3 times before gracefully reporting an error message. You will need to test that this robustness tactic actually works as expected. 

We recommend to add this robustness tactic to all interactions with the GitHub API, **but for this assignment, it is sufficient to implement and test it for a single function of your choice.**

# Deliverables

Submit your solution as follows:

1.	All the code of implementation and tests regarding both steps should be in your GitHub classroom individual repo; tests should be executed automatically with Gradle.
2.	Submit a short report with explicit subsections (< 2 pages, hard limit) as a single PDF to eClass, describing the design decisions that you made to enable testing. Specifically: 
	a.	Describe which elements you chose to mock and why and where mocking was not necessary or useful.
	b.	Describe how you refactored the code to make it easier to test.
	c.	Explicitly mention which function you chose to implement robustness for and describe how you assessed that your testing w.r.t robustness is adequate.
	d.	If you had more time and resources, would you propose additional changes to make testing easier?
	
**Please indicate your repo url in your report**

# Requirements and Restrictions

You must follow good testing practice.

* You must actually test the code that you are trying to test.
* You should not mock your own code (with the exception of unavoidable wrapper classes: see Hints section below).
	* You should only be mocking the API provided by the "github-api" package.
* All methods and classes in your production code should be in use by the production code.
	* Do not add special methods, constructors, or classes that are only ever called by your testing code.

# Grading

Tota: 35 marks

* Step 1 (15 marks, 3 for each functionality)
* Step 2 (10 marks, 5 for adding robustness + 5 for testing it)
* Report (10 marks)

# Hints

You will need to change private visibility to protected visibility in order to access them from your testing code. 

Mockito and github-api both use Java bytecode manipulation. Mockito does this to help inject dependencies. However, this can come into conflict with methods in the github-api that are decorated with `@WithBridgeMethods`. One example is the `GHIssue.comment` method. This can result in an error like `Date cannot be returned by getCreatedAt() getCreatedAt() should return String`. This error message doesn't really make sense because the application bytecode was manipulated *after* being compiled. In order to solve this, you will need to create a wrapper for `GHIssue`, use the wrapper in the production code, and then mock the wrapper instead of the wrapper class from github-api in the test code. You will also need to do this for any other methods that are decorated with `@WithBridgeMethods` in the [github-api code](https://github.com/hub4j/github-api/tree/main/src/main/java/org/kohsuke/github). So if you get a strange error with impossible types, check the code of github-api to see if it uses such a decorator, and add a wrapper class as needed. This is not the only way to solve this problem, but it's the easiest way we've found so far. *Wrapper classes shouldn't do anything but just call the class they are wrapping.*

Usually you should avoid modifying the production code to add wrappers that are only necessary for the test code to work. However, in this case it is unavoidable becuase the methods mockito and the github-api code use are in conflict. Similar conflicts can also arise in other programming languages such as Python.

Keep in mind that there are many different ways to solve everything in this assignment. For example, mockito has `@` decorators that can make your code a lot cleaner than the provided sample code.

You can use the `try (MockedConstrcution` pattern to intercept any constructor. This is using a Java feature called [try-with-resources](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html). But its not necessary to do unless the "new" you're trying to intercept is in the production code (or somewhere inside of github-api). For any constructors called in the testing code, you can just `mock(Whatever.class)`.

Copyright 2021, 2022 Dr. Sarah Nadi. Copyright 2023, 2024 Dr. Hazel Campbell. All rights reserved.
