Title: Group Assignment 2: Testing
date: 2024-01-30
tags: labs, policy, grading
authors: Hazel Victoria Campbell, Sarah Nadi
status: published
----

[TOC]

# Overview

In this project, you will extend the Tartan Home system with new functionality
and test it for functional correctness, code quality, and quality attributes.
You will conduct this testing at multiple levels (e.g., unit, integration, and
system) primarily to verify functional correctness of existing and new code.
You may also need to modify your testing infrastructure from G1, as needed. The assignment
requires teams to extend the system to support a new smart door lock with
several features and test that functionality. G2 has two parts.

The learning goals of this group project are:

- Learn to to setup and manage a continuous testing strategy and supporting
  technologies.
- Gain experience using different test case design techniques.
- Select and integrate appropriate testing techniques throughout the
  engineering process, using appropriate technologies.
- Select and assess various measures, including but not limited to code
  coverage, for the adequacy of a test suite.

The following requirements must be satisfied to start this project:

- The team is familiar with collaborative development and code review
  features of Github (a quick recap will also be provided in the lab).
- A development environment with Java, gradle and docker support,
  preferably together with a correctly configured IDE like Eclipse or
  IntelliJ that allows to execute unit tests and perform coverage analysis
  on Java projects.
- Note that you must continue working on the same repository you created through GitHub classroom for group project 1. 

You will also likely need several additional tools to complete this assignment.
Please identify and describe these tools in your report.


# Part 1: Improve Test Suite

In G1, you were still starting out with Tartan and did not know of all the techniques that can help you choose meaningful test cases and also assess the quality of your tests. Additionally, you only implemented one test per feature. 

In the first part of this assignment, your task is to improve the quality of your test suite for the four rules you chose in G1 as follows:

1. Use blackbox testing techniques to create better test cases and corresponding oracles (i.e., the concrete input values and expected output in your tests). You are advised to carefully read Tartan's specification and decide on whether there are additional scenarios you need to test for (e.g., now is time to think about whether the rules interact and if there are edge cases you need to think of). When selecting concrete oracles, some of your options include boundary value testing, random testing, or strong/weak equivalence class testing. You may think of other strategies too. Although you will work on your selected four rules for the blackbox testing, you need to think about all variables (old and new) of the evaluateState() function and how changing one particular state might affect your selected rules.
2. Use whitebox testing techniques to evaluate and improve the adequacy of your test suite. In this case, you are asked to write more tests that improve the coverage of your test suite to 80%.

It does not need to be 80% of the entire system: you only need 80% coverage of the methods that implement your four rules. 

Please refer to the code coverage tutorial posted on eClass and discussed in the lab to see how you can configure your coverage measurement tool to measure coverage only for your selected features. However, you must include *at least* all methods your blackbox tests interact with either directly or indirectly.

## Acceptance criteria for Part 1

The following criteria must be satisfied for Part 1 to be accepted as
complete. A description of the report you must submit is provided at the end.

| Criteria | Grade |
|:-------- |:-----|
| Whitebox and blackbox test design and selection plans are completed and explained. | 10 |
| Automated measurement of coverage with each build is implemented | 5 |
| All tests pass. | 10 |
| Tests must achieve at least 80% statement and 80% branch coverage for the *features selected to test.* | 15 |


# Part 2: Implementation and Verification of a Smart Door Lock

Tartan Inc. would like your team to implement the software logic for a new smart
door lock. The smart door lock hardware allows the door to be locked and
unlocked automatically using a passcode, and it will provide many "smart"
features that users can configure for additional security or convenience. Note that opening/closing the door is different from locking/unlocking a lock. The former refers to the physical state of the door while the latter refers to the state of the deadbolt on the door.
Specifically, the smart lock must support the following features that users
can enable or disable:

- *Electronic Operation:* If a person requests a lock or unlock operation
  from an access panel, first check if that operation requires a
  passcode. If it does, read and check the passcode. If the passcode is refused, send a message to the access panel. Otherwise, perform the requested operation.
- *Keyless Entry:* When sensors detect a resident arriving on the
  property (e.g., proximity of a registered cell phone), automatically unlock the door.
- *Intruder Defense:* When sensors in the house detect the possible presence
  of an intruder, lock the door and send "possible intruder detected"
  messages to the access panels. Keep the door locked until the sensors
  provide an "all clear" signal, at which time "all clear" messages are
  sent to the access panels.
- *Night Lock:* Residents configure the time when night begins and ends. At
  night, automatically lock the door and always relock it if it becomes
  unlocked at any point during the night.

An access panel is one of these: <br>
<img id="access-panel" alt="access panel" src="{attach}adt-access-panel.jpg" style="width: 50%;">
For the access panel you can add the functionality to the frontend, since we don't have any physical access panels.
Make sure that your messages are shown on the frontend log of the application.
You can append the access panel messages to your log in your code and make sure it's showing up on the frontend.

Note that the above feature requirements may be ambiguous. In addition, features
may interact and the door lock should behave in a reasonable way, which can be
resolved with timers, priorities, or other mechanisms. For example, what
happens or should happen if an intruder is detected and a resident arrives at
the door? You should ask for clarification about requirements if needed and
explicitly document all assumptions you make about interactions.

Integrate the smart door lock and its features with the current system and test
it thoroughly. You can add additional sensors and actuators to the house, if
needed.

**While developing the new door lock features, you must follow a test-driven approach.**
Use Pull Requests to integrate each new functionality and have another team member review your code. **Each team member must perform a code review of
at least 1 PR.**

To make it easier for us to spot your test-driven development, you must make your commits
using a specific pattern that shows that you have worked using TDD. Make a
git commit after each of the following steps:

- Red: Write a test that fails. Make a commit with the word "RED" at the beginning of the commit message.
- Green: Change the implementation so that the test succeeds. Make a commit with the word "GREEN".
- Refactor: Rewrite the code. Make a commit with the word "REFACTOR". Your tests must still pass after this change.

You must conduct unit testing on the new code and carefully measure coverage.
However, given that this is a new feature, you should also perform integration (i.e., tests that combine multiple classes/functionality) and system testing (i.e., end to end testing that treats the system as a black box). You must document the integration and system testing
procedures in your report. 

### Acceptance criteria for Part 2

The following criteria must be satisfied for the assignment to be accepted as
complete.

| Criteria | Grade |
|:-------- | :----|
| Requirements for the smart door lock are documented. The documentation format is up to the team, but should be clear and complete and includes any assumptions the team made. | 10 |
| The software for the smart door lock successfully builds, runs, and implements stated requirements. | 10 |
| Integration and system testing strategy is implemented and described | 10 |
| Tests must achieve at least 80% statement and 80% branch coverage for ***new*** code. | 15 |
| The mutation score for the tests related to the new door lock functionality should be 90%| 10 |
| Test-driven development has been followed | 5 |
| New features underwent code review | 5 |


# Report for Parts 1 & 2

Create a report as a single **PDF** file that describes your verification
activities, decisions, and results for both the existing functionality and the
new door lock (max. 4 pages of text, not including screenshots/tables etc). You must upload your report to eClass by the specified deadline. While marking, we will verify all acceptance criteria by checking both your report and code repository.
**The final version of your code for all parts of this project must be in the master branch and tagged as `G2_Done` by the deadline.**

The following describe the required details of the report:

- **Part 1**:
	- **Chosen Rules**: For completeness, restate the four rules you chose for part 1 (they should be the same as those from G1).
	- **Testing plan and test cases**: Describe the
  process you used to design test cases and provide an overview of the tests
  you wrote. How were test cases designed? How were test values selected? Which
  testing techniques did you use (i.e. random testing, combinatorial testing,
  BVA, other)? Mention how much additional testing you needed to add in G2 when compared to G1. Finally, provide a pointer to the actual test classes/methods scripts in your repository.
  - **Coverage**: Provide a screenshot of your coverage report (you can focus only on the relevant parts of the system). While marking, we will look into the actual report ourselves and make sure you satisfy the coverage criteria.
- **Part 2**:
	- **Clarified requirements for smart door lock**:
  Describe all assumptions you made about the requirements of the smart door
  lock system and its features.
  - **Software development processes**: Briefly indicate
  the role of each group member in this process, describe how you planned and
  organized the design, development, and evaluation of the smart door lock.
  Include a description of how you coordinated implementation and
  testing.
  - **Overall testing strategy and implementation:** . Indicate where your unit, integration, and system tests are implemented. Mention what you chose to test for integration testing as well as system testing. Which tools/frameworks/techniques did you use to implement your integration and system testing?
  - **Coverage and mutation score:** Provide a screenshot of your coverage report (you can focus only on the relevant parts of the system). While marking, we will look into the actual report ourselves and make sure you satisfy the coverage criteria. Also, provide a screenshot of your mutation score report. Please mention 2-3 examples of initially live mutations (i.e., mutants that your test suite did not initially kill) and how you improved your test suite to kill these mutants.

# Grading Summary

In total, this project is worth 120 points with the following allocation:

- Part 1 (improving test suite): 40 points
- Part 2 (implementation and verification): 65 points
- Report: 10 points
- Peer assessment: 5 points (Assigned individually)

The report is graded based on its presentation, organization, and how clearly things are described. All the items described in the Report section above must appear in the report.

Each member must assess their team members' contributions on eClass. This is worth 5 points of the total assignment grade and is confidential (results go to the course staff). Note that if we find big discrepencies in contributions or if one team members is negatively rated by all other team members, then we will investigate and regrade team members as needed.

# Questions You Should Be Able to Answer After This Assignment

* What is a unit?
* How does TDD differ from standard types of testing?
* What is an Oracle?
* What might you need to change in the System Under Test in order to make good use of unit testing?
* What makes black box testing different from white box testing?
* Why might we want to use black box testing?
* What is the purpose of unit-testing?
* What are equivalence partitioning and boundary value analysis?
* Why do we use TDD? What is its purpose?
* Can we always have 100% code-coverage?
* What are the different types of coverage criteria?
* Does 100% coverage mean we are bug-free?
* Does 100% MCDC coverage mean we are bug-free?
* Can we prove that we’re 100% bug-free?
* In TDD, Why do we go for RED first?
* How did you handle interactions in the requirements in part 2?
* How did you test for intereactions?
* Do the computed adequacy criteria give you confidence that your software is thoroughly tested and of adequate quality?
* If you could pick your own goals for test adequacy measures, what would you aim for?
* Which testing techniques were most effective for you and why?
* Which techniques were less effective and why?
* Did mutation testing help you find weaknesses in your test suite? Can you give an example?
* If you had to conduct a similar project again, would you change any of your testing or planning strategies?
* What were the challenges you faced and how did you solve them?

Copyright 2021, 2022 Dr. Sarah Nadi. Copyright 2023, 2024 Dr. Hazel Campbell. All rights reserved.
