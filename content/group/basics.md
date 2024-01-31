Title: Group Assignment 1: Basics
date: 2024-01-30
tags: labs, policy, grading
authors: Hazel Victoria Campbell, Sarah Nadi
status: published
----

[TOC]

# Overview

The goal of this first group project is to familiarize yourself with the Tartan Home system, which you will eventually extend with new functionality
and test for functional correctness, code quality, and other quality attributes.

The learning goals of G1 are:

- Familiarize yourself with technologies/concepts such as gradle, DropWizard, Hibernate, and RESTful Web services.
- Learn to to setup and manage a continuous integration strategy and supporting
  technologies.
- Get experience adding tests to an existing system

The following requirements must be satisfied to start this project:

- A development environment with Java, gradle and docker support,
  preferably together with a correctly configured IDE like Eclipse or
  IntelliJ that allows to execute unit tests and perform coverage analysis
  on Java projects. (IntelliJ is recommended but not required)
- All members of the team must accept the assignment on GitHub classroom on the following link [https://classroom.github.com/a/v-Nv1id7](https://classroom.github.com/a/v-Nv1id7). This will create the private repository your team will work on. Please note that your teams are already created on eClass. Make sure to join your assigned team. **The first person from your team to accept the assignment on GitHub classroom will create the team there. Use the same team name as on eClass (e.g., Group1, Group15 etc)** 

You will also likely need several additional tools to complete this assignment.
Please identify and describe these tools in your report.

For all submissions, make sure to explicitly mention your group number and all group memeber names and CCIDs, as well as your team's GitHub repo. You should also edit your repo's ReadMe file to include your group name and members.

# Part 1: Verification of Existing Functionality

Write *four* test cases for Tartan

The following describe Tartan's rule for making decisions about the house state. Your first tasks is to select ***four*** of these rules and assess that they are correctly implemented. You will write one unit test for each of selected rule.

- **R1:** If the house is vacant, then the light cannot be turned on.
- **R2:** If the alarm is enabled, and the door gets opened, then sound the alarm.
- **R3:** If the house is vacant, then close the door.
- **R4:** If the alarm is enabled and the house gets suddenly occupied (i.e., someone is detected by the proximity sensor), then sound the alarm.
- **R5:** If the house is empty, then start the away timer.
- **R6:** When the away timer expires, then turn off the light, arm the alarm, and close the door.
- **R7:** If the house becomes occupied while the alarm is disabled, then turn on the lights for the legitimate user.
- **R8:** The alarm can be disabled *only* when the house is occupied (i.e. it cannot be disabled remotely).
- **R9:** The correct passcode is required to disable the alarm.
- **R10:** If the target temperature is greater than the current temperature, then turn on the heater. Otherwise, turn off the heater
- **R11:** If the target temperature is less than the current temperature, then turn on the air conditioner. Otherwise, turn off the air conditioner.
- **R12:** The heater and the dehumidifier cannot be run simultaneously.

At this point, you need to only implement one unit test for each selected rule. In G2, you will be asked to implement additional tests as needed. For the purpose of G1, you can assume independence between the rules (i.e., you do not need to think about situations that combine multiple rules). You will think about that for G2. 

If you find that any of the functionality are not correctly implemented, you must indicate the problem you found in your report and how you fixed it.

# Part 2: Test Automation Infrastructure

Now that you have written your initial tests and understand how to build and run Tartan, you will set up the infrastructure necessary to automate building and testing. You will set up and configure
[GitHub (GH) Actions](https://github.com/features/actions) in your own
repository to be used for the rest of the semester. 

## Infrastructure Setup

Set up and configure GH Actions workflow in your repository. As a minimum, your team should:

- Set up GH Actions in the repository.
- Automate the build and tests of the Tartan Home system using workflows (use the tests you wrote in Part 1 to try out and demonstrate the infrastructure)
- Configure GH Actions to automatically trigger a new build whenever changes
  are pushed to your GH repository (e.g., main branch).

At this point, you are also welcome to explore additional GH Actions that may provide useful functionality, for example, actions that show statistics, test coverage, or track performance results. You may find this
[link](https://github.com/sdras/awesome-actions) useful if you want to set up
additional workflows. This is not required for G1 but may prove useful for your next group projects.

# Acceptance criteria for G1

Submit a short (max. 3 pages) informal **PDF** report on eClass that:
- mentions the four rules you chose and the name/location of the corresponding tests
- _briefly_ describes your infrastructure setup (i.e., the list of GH actions/workflows you set up and how these workflows build the code and run the tests). 
- includes one or more screenshots that show (1) a successful build, (2) a failing build, and (3) the passing tests from Part 1. 

## Notes on Screenshots

1. For the passing build, it is enough to share a screenshot of a successful Github Actions workflow run.
2. For the failing build, it needs to be a result of a build failure (e.g., due to compilation issues) or test failure (i.e., a test did not pass). Failures caused by wrong setup of your workflow (e.g., permission issues, "No such file or directory" errors, etc.) are NOT examples of a failing build. These are examples of a failed setup.
3. For the passing tests, the screenshot must include the name of the passing test. Thus, it needs to be screenshot of either an IDE test execution window or the test report that gets generated by Gradle (located in the file `build/reports/tests/test/index.html`) such that name of the passing test can be seen.

The following criteria must be satisfied for G1 to be accepted as
complete. 

| Criteria                                                                    | Grade |
|:--------------------------------------------------------------------------- | :--- |
| Four unit tests that verify the functionality of three rules and run successfully (i.e., passes) | 40 |
| A description of any bugs found in the system through the test & how they were fixed as applicable. If no bugs found, an explicit statement is required. | 5 |
| The test infrastructure is set up with automated building and testing. | 10 |
| Github Actions platform reports when the build (i.e., either compilation or tests) is passing/failing.                     | 10 |

**Please tag your code with `G1_Done`**


# Grading Summary

In total, G1 is worth 80 points with the following allocation:

- Acceptance criteria: 65 points
- Report: 10 points
- Peer assessment: 5 points (assigned individually)

The report is graded based on its presentation, organization, and how clearly things are described. All the items described in the Acceptance Criteria section above must appear in the report.

Each member must assess their team members' contributions on eClass. This is worth 5 points of the total assignment grade and is confidential (results go to the course staff). Note that if we find big discrepencies in contributions or if one team members is negatively rated by all other team members, then we will investigate and regrade team members as needed. 

Copyright 2021, 2022 Dr. Sarah Nadi. Copyright 2023, 2024 Dr. Hazel Campbell. All rights reserved.

