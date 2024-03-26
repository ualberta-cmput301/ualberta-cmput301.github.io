title: Group Assignment 5: Technical Debt
date: 2024-01-30
tags: labs, policy, grading
authors: Hazel Victoria Campbell, Sarah Nadi
status: published
----

[TOC]

# Overview 

To complete your evaluation of the Tartan Home Platform and your enhancements, you will assess its technical debt and existing issues using SonarQube with an emphasis on how difficult the software will be to maintain going forward. 

Major development is over and the software is nearly ready to ship. As part of project wrap-up, management wants to assess the overall quality of the project based on SonarQube’s metrics and recommendations so they can correct lingering issues and reduce technical debt. 

The goals of this project are: 

*	Gain experience with a quality management tool.
*	Use technical debt to assess the quality of a software system.
*	Reflect how design and development decisions made impact quality.

# Tools

You will use SonarQube ([http://www.sonarqube.org](http://www.sonarqube.org)) to analyze your software for this project. 

# Task

In this project, you will evaluate the technical debt in the Tartan Home Platform. Given sensitive customer data in the system, the sponsor is still concerned about the possibility that hackers might spy on, or meddle with a home. On the other hand, after extending the system over the past few months, and with more enhancements expected in the future, the team is more concerned about how difficult it will be to change the code.  

Your goal is to evaluate and describe the current technical debt to the project's stakeholders and argue whether paying back (part of) the debt now is essential or not. To do so, you will evaluate your project with SonarQube, but you may choose to perform additional assessments.

To load the Tartan Home Platform into SonarQube, do the following: 

*	There are a number of ways to import the Tartan Home Platform into Sonar. Examples include: 
	* Use a Sonar Scanner: [https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner-for-gradle/](https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner](https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner-for-gradle/))
	* (Recommended) Use Sonar Scanner with gradle: [https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner-for-gradle/](https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner-for-gradle/). You may want to show the results of SonarQube in your CI build, but this is not required for this project.
*	Once loaded, open the project in SonarQube or view the results of the scan in your CI build (If you installed SonarQube locally this will be through a web browser; default url: [http://localhost:9000](http://localhost:9000)). 

# Deliverables

This is the final assignment that involves analysis and development of the Tartan Home Platform. The focus is on reflecting on the quality assurance strategies used throughout the semester and the use of tools like SonarQube to assess and operationalize technical debt.

Your team must submit a report on the technical debt in the project. You will also present your findings in class. Your report should report the following:

1.	Evaluate the quality of your project. You must analyze and explain the technical debt that may exist in your project. Make sure to include the results/snapshots from SonarQube.
2.	Evaluate the usefulness of SonarQube's reports. 
	* Do the ratings (Maintainability, Reliability, and Security) provided by SonarQube correspond to your intuition/impression of working with Tartan? 
	* Which other SonarQube metrics or graphs were useful for your analysis of technical debt? 
	* Which parts of your the code base (i.e., classes, modules, packages etc) were ranked the best and worst?
	* How do the new features or changes you made compare to the existing code that you started with? Have you added more debt or have you paid back some debt? (you will need to compare technical debt of the original Tartan code to the current version after the changes)
3.	Similarly, evaluate whether your current CI pipeline (without use of SonarQube) and its logs are useful for assessing technical debt.
4. Based on the current metrics, would you advise your team to pay back (part of) the technical debt right now before developing the new features in the pipeline? Why or why not? Make sure to elaborate your recommendation.
5.	How would you adjust SonarQube or GitHub actions (or any equivalent CI pipeline) to assess technical debt in the future? Would you continue to use these tools? Would you introduce/eliminate rules or reports? Change quality profiles and quality gates? Why? 

The report should be no more than five pages in length.

You must also prepare an **8 minute presentation** that summarizes the report, addressing your team’s evaluation of technical debt in your system and a reflection on the overall quality of the Tartan Home System. **All group members are expected to be part of the presentation.** Note that your presentation will be in the lab before your report is due. Your presentation should cover the following:

* Start with a **quick** overview of your CI pipeline and all the quality tools/measures you incorporated in your Tartan system throughout the term. Some teams may have chosen to use additional tools beyond what was required in the project assignments. Please discuss this tools and the rationale for using them, as applicable.
* Present the above 5 points from your report. You do not need to present them in the same order, but you do need to provide a good summary of the complete reflection process. Choose the most entertaining way to do this.
* Please upload a pdf of your slides to eClass along with your report.

# Grading & Expectations

This assignment is worth 90 points, allocated as follows. 

Note that we will use both the content of your report and presentation to grade the following components.

*	Quality evaluation using SonarQube (points 1 & 2 above): 30 points 
*	Discussion on using your current CI pipeline for technical debt assessment: 10 points
*  Advice on paying back current debt: 15 points
*	Discussion of metrics and tool adjustments/customizations: 10 points
* Peer-rating of group members: 5 points (assigned individually). Ratings are confidential (results go to the course staff). Note that if we find big discrepencies in contributions or if one team members is negatively rated by all other team members, then we will investigate and regrade team members as needed.

There will be an additional 20 points allocated to the presentation quality, based on the following crtieria:

* Slides are well-designed (readable fonts, not cluttered, not completely text based, meaningful titles, slide numbers etc)
* All team members speak clearly and loudly in an engaging way
* Presentation flows well and the audience undertsands what is presented at each point
* Use of well-explained figures/charts etc to backup presented points

**Points will be deducted if your report is unstructured or not understandable.**

Copyright 2021, 2022 Dr. Sarah Nadi. Copyright 2023, 2024 Dr. Hazel Campbell. All rights reserved.
