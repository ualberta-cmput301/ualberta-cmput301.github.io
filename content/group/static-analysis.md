title: Group Assignment 4: Static Analysis
date: 2024-01-30
tags: labs, policy, grading
authors: Hazel Victoria Campbell, Sarah Nadi
status: published
----

[TOC]

# Overview

The learning goals of this project are: 

*	Gain experience using a static analysis tool.
*	Understand what types of defects can and cannot be found with static analysis.
*	Critically evaluate the results of static analysis tools.

You will run a static analysis tool on the same Tartan project your group has been using. 

# Resources

You will use the following static analysis tools to analyze your Tartan codebase for potential problems:

- SpotBugs
- PMD
- ErrorProne

## SpotBugs

There are a couple of ways to integrate [SpotBugs](https://spotbugs.github.io/)

- Through [Gradle](https://plugins.gradle.org/plugin/com.github.spotbugs)
- Standalone by downloading the binary distribution and running it as a Java application. See [installing](https://spotbugs.readthedocs.io/en/stable/installing.html) and [running](https://spotbugs.readthedocs.io/en/stable/running.html). 
- As a [plugin for IntelliJ IDEA or Eclipse](https://spotbugs.readthedocs.io/en/stable/links.html#ide-integration)

## PMD

Follow [the guide for PMD Gradle Plugin](https://docs.gradle.org/current/userguide/pmd_plugin.html) to integrate [PMD](https://pmd.github.io/) to your build system. You can also use the [CLI option](https://pmd.github.io/latest/pmd_userdocs_installation.html#running-pmd-via-command-line) which does not require you to make changes to your `build.gradle` file.

## ErrorProne

Use [the guide for Gradle ErrorProne Plugin](https://github.com/tbroyer/gradle-errorprone-plugin) to integrate [ErrorProne](https://errorprone.info/) to your build. Please pay extra attention to the [Java 8 support](https://github.com/tbroyer/gradle-errorprone-plugin#jdk-8-support) section as ErrorProne requires at least JDK 9.

# Task

Run SpotBugs, PMD and ErrorProne on your Tartan system and analyze the results. Specifically:

1. (5 marks) Report how many errors/warnings were reported by each tool and in which categories (note that the category names or how errors/warnings are categorized in each tool may be different for each tool).
2. (5 marks) Report the similarities and discrepencies between the tools. Are there errors/warnings that one tool reports but the other doesn't (give at least 3 examples, if available)? Are there error/warnings that all three tools report? (give at least 3 examples, if available)
3. (5 marks) Report which Java class(es) from Tartan seems most problematic. Explain your result.
4. (60 marks total) Select 10 reported problems, distributed across the three tools, to analyze in more detail. For each problem, report
	* (2 marks) The identifying information for the bug, including its category, priority, file name, and line number.
	* (1 mark) A one-sentence description of the problem
	* (2 marks) A characterization of the bug in terms of whether it is an actual problem, false positive, or irrelevant true positive. Explain your reasoning.
	* (1 mark) How you fixed the problem (if you decided it was actually a problem)

(5 marks) Peer-rating of group members. This is assigned individually. Note that if we find big discrepencies in contributions or if one team members is negatively rated by all other team members, then we will investigate and regrade team members as needed.

Your submission will include a PDF report with the above information. The total points for this assignment is 80 marks.

# Questions you should be able to answer after this assignment

* What is a false positive?
* What is a false negative?
* Are there problems in the code that the tool did not catch?
* Does running a static analysis tool replace the need for testing?

Copyright 2021, 2022 Dr. Sarah Nadi. Copyright 2023, 2024 Dr. Hazel Campbell. All rights reserved.
