Title: Group Assignment 3: Testing in Production
date: 2024-01-30
tags: labs, policy, grading
authors: Hazel Victoria Campbell, Sarah Nadi
status: published
----

[TOC]

# Overview

In this project, you will build infrastructure for Tartan in order to conduct tests in
production. First, you will deploy your application with [Docker
containers](https://www.docker.com/resources/what-container) and automate
deployment into production as well as making it easy to roll back changes.
Second, you will extend the project and build an AB testing infrastructure that
can be used to assess specific changes.

Learning goals:

- Design an AB-testing infrastructure to run tests in production.
- Deploy the system through a virtualized infrastructure and support rapid updates and rollback operations with test automation.
  
Note that you can continue to work on the same Tartan Home repository you created through GitHub classroom for the previous projects. Please check eClass for deadlines.

# Tasks

## Continuous deployment

Having learned about continuous deployment, members of your company are curious
to try it. You will investigate Docker containers and run your infrastructure
in containers. You can also run the house simulators in Docker containers if
you like. Because your company does not have in-house server machines, your
company is going to acquire VM resources from
[Cybera](https://cloud.cybera.ca/).  Since Cybera uses
[OpenStack](https://www.openstack.org/software/) to manage its computing
resources, you will also use it to create your own VM instance. After creating
and configuring that instance (e.g., associate floating (public) IP address,
install Docker), you will deploy and run your containers there. Note that we
already provided a setup for Docker (`docker-compose.yml` file) with the
original release that you are welcome to use or modify.

You will need to extend your build and test automation, such that Docker containers for all
backend services (controller, database, and possibly additional services you
may create) are *created automatically* every time you push a commit to GitHub
and it passes all tests. You can either *launch* the new containers
automatically, replacing the currently running ones, or provide a lightweight
mechanisms where a human operator can launch a new version with a single button
or command-line instruction. (The house simulators are not part of the backend
and should usually continue running while the controller is updated.)

Finally, implement a technique for how to undo a release and revert back
to the previous version. Similar to releasing new versions, undoing a release
should be possible with a single button click or command-line instruction. Make sure to test your roll-back technique and to fully document the exact steps that should be done to perform a roll back.

For the purpose of this assignment, it is not necessary to roll out changes
incrementally or build a canary test infrastructure. However, you may possibly
need to slightly modify controller or houses to deal with short-term connection failures during updates.

## AB testing

In addition to automating deployment, you will extend the Tartan Smart Home
system with a **reporting feature** that sends customers weekly or monthly reports
about how they use their system. You will then design an experimentation
infrastructure in which you test different versions of the reporting "in
production" to see whether customers change their behavior.

You have significant flexibility in the assignment in deciding what kind of
reporting you add and what kind of experiments you want to run. For example,
you may find inspiration from decades of
[studies](https://www.sciencedirect.com/science/article/pii/0378778894009124)
that analyze what kind of information in electricity bills actually encourage
customers to reduce their electricity consumption, but you can also report on
other behavior of the smart home, such as temperature, door locking status,
etc. Note that building the experiment infrastructure is more important than
the actual experiments and certainly more important than whether your new
reporting feature looks pretty.

In this assignment, you may want to change multiple parts of the system or may
be able to work only with modular additions (e.g., adding a new microservice
for reporting and another one for configuration and analysis). Given that you
cannot actually test with a production system yet (the team developing the
hardware for the houses is still not ready, \*sigh\*), you may want to change the
simulation infrastructure to have more houses and houses with different
behavior to test your infrastructure in simulation.

Specifically:

- Build a reporting system that creates reports for each customer with a Tartan Smart Home installation, reporting an aspect of your choice.
- Build an experimentation infrastructure that (a) allows you to send different
  versions of the reports to different customers or at different times, (b) analyzes whether these changes have an effect on outcomes of how these customers use the system. You may need to modify how you track different customers and you may need to collect additional data about outcomes.
- At the end of the experimentation period, generate some form of visualization (e.g., chart, graph, table whether as an html page or as a downloadable file) that shows which report variant was sent to which customer and how it affected them. For example, perhaps they now turned their lights off more often or decreased the average temperature of their home.

## Acceptance Criteria

The following criteria must be satisfied for the assignment to be accepted as
complete.

| Criteria (Continuous Deployment) | Grade |
| :------------------------------- | :----|
| The system, including the simulation of houses and the new experimentation infrastructure is deployed with Docker containers | 10 |
| All changes that pass the automated test suites are *automatically built* as deployable Docker containers | 15 |
| The *deployment* of newly built versions of the docker containers on the virtual machine is either fully automated or can be done with a single command that is described in the repository's README file or wiki. | 20 |
| Reverting the running system to the previous version can be achieved with a single command that is described in the repository's README file or wiki. | 15 |

| Criteria (AB Testing) | Grade |
| :-------------------- | :---- |
| A reporting system has been implemented that can periodically send reports to customers. | 15
| An experimentation infrastructure has been implemented that tracks which customers should see which variants of the software. | 20 |
| An analysis infrastructure has been implemented that can evaluate the outcome of experiments (given one metric, how did customer's behavior change)| 15 |
| An experiment has been conducted using the experimentation infrastructure, sending different variants of the report to different customers and observing different outcomes. | 20 


# Deliverables

## Code and Scripts and Documentation

Commit all infrastructure configuration and scripts to your git repository. Commit your code of your reporting feature and experiment
infrastructure to your git repository. **The final version of your code should be
in the master branch of each repository, and it should be tagged as `G3-done`**.

Include technical documentation of how to launch containers, update containers after a build, and revert containers as part of your repositories README.md file or GitHub wiki. If you choose to use the wiki, make sure that you state that in the README. 

## Report

Create a report as a single PDF file that describes your design and experiments
(figures, screenshots, etc do not count toward the page limit). Describe the
following:

- **Reporting feature** (<1 page text): Describe your reporting feature and the
  goal for which you are optimizing (e.g., reducing energy consumption);
  include an example of a report.
- **Experiment design** (< 1 page text): Describe your experiment(s): what are the
  experimental conditions (independent variables) and measured outcomes
  (dependent variables) and how you measure those.
- **Experimentation infrastructure** (< 1 page text): Describe how you assign
  experimental conditions: how you implement experimental conditions (e.g.,
  branches, feature flags); how you assign control and treatment groups; and a
  short justification why you chose this implementation/design.
- **Analysis infrastructure** (<1 page text): Describe how you analyze the outcome of the experiment. We encourage you to include a screenshot showing
  the outcome of your experiment.
  
  
# Grading Summary

This project is graded out of 155 points according to the following breakdown. 

* Continuous Deployment: 60
* AB Testing: 70
* Report: 10
* ReadMe: 10
* Peer assessment: 5 (assigned individually)

The report is graded based on its presentation, organization, and how clearly things are described. All the items described in the Report section above must appear in the report. The ReadMe is graded based on whether all instructions we need to run things are there or not (Be very explicit. Do not assume we know how to run things)

Each member must assess their team members' contributions on eClass. This is worth 5 points of the total assignment grade and is confidential (results go to the course staff). Note that if we find big discrepencies in contributions or if one team members is negatively rated by all other team members, then we will investigate and regrade team members as needed.

Copyright 2021, 2022 Dr. Sarah Nadi. Copyright 2023, 2024 Dr. Hazel Campbell. All rights reserved.
