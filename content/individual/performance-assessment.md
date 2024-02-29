Title: Individual Assignment 3: Performance Assessment
date: 2024-02-29
tags: individual, policy, grading
authors: Hazel Victoria Campbell, Sarah Nadi
status: published
summary: Individual Assignment 3: Performance Assessment
----

[TOC]


# Overview

In this assignment, you will assess the performance of a given system and
reflect on how such assessment can be done effectively.

The learning goals of I3 are:

- Deciding which performance concerns are important for a system    
- Deciding between different approaches to performance assessment and understanding their limitations
- Learn how to use JMeter for load testing and performance assessment

# Performance analysis of book website

In this assignment, you are being asked to assess the performance of a web site
that can list and search book covers (with title, author, categories,
publication date, cover image, etc.), for which we provide a runnable (through
Docker Compose) setup in a [GitHub repository](https://github.com/cmput402-w23/bookstore)
with about 800 book covers. This assignment intentionally gives you a lot of
flexibility in deciding what performance characteristics (e.g., throughput,
latency) are important and how they should be assessed. Make sure to assess
performance of all [endpoints](https://github.com/cmput402-w23/bookstore#endpoints).
Justify your decisions, conduct a reasonable performance assessment with
limited time, and discuss what additional steps you would take with more time.

The main deliverable is a report (4 pages, max) which should cover the
following questions:

- **Performance concerns:** What are (likely) important performance concerns or
  requirements for the system? Justify your answer.
- **Measures:** How can those performance concerns be assessed? (define the
  measure, be clear about units, characterize how you would distinguish good
  from bad performance with this measure).
- **Measurement process:** What measurements did you conduct to collect the
  measures in the previous point and how? Justify your design (e.g., overall
  setup, workload selection) and describe your process briefly but with
  sufficient detail to reproduce it. You can attach screenshots of your JMeter
  test plan, if that helps.
- **Measurement results:** What were the results from your performance
  assessment? Discuss how well the system achieves the performance qualities.
  Include plots (charts, graphs, etc.) if they help your discussion of results.
- **Next steps:** If you had more time, what additional steps would you take
  for performance assessment of this system? Would you automate tasks or
  integrate them in the development process? Why/why not?

## Notes

**Resource limits.** You might see resource limits set up in
`docker-compose.yml` file. That is done on purpose. Do not modify the file,
otherwise the results might not be what we expect. You should only work with
JMeter and not change anything in the code. However, you are welcome to explore
the source code, as well as the data set, if you want to.

**Fatal errors**. It is possible that the application will crash due to too
heavy load.  That's an example of stress testing where your goal is to estimate
what is the maximum load that the system can handle before crashing. If you
experience this issue, try to determine what is the maximum load it can handle
before failing (e.g., number of requests) and mention that in the report. You
do not need to find the exact number (e.g., "1227 requests"), but try to be as
precise as possible (e.g., "about 1200 requests").

# Acceptance criteria for I3

Submit the report as a **PDF** (max 4 pages including any screenshots, plots,
etc.) with clear subsections to eClass. Keep all sections under half a page if
possible, except for the process description, which might be longer and might
include additionally screenshots or scripts if that simplifies your
description.

The following criteria must be satisfied for I3 to be accepted as complete.

| Criteria                                                                    | Grade |
|:--------------------------------------------------------------------------- | :--- |
| Reasonable, comprehensive, and clearly justified performance goals. | 5 |
| Well defined performance measures. | 5 |
| Well described and reproducible measurement process. | 10 |
| Clearly described measurement results (in a form understandable by the target audience of your performance goals). | 10 |
| A plausible discussion of next steps. | 5 |


# Useful resources

- [How to Use JMeter for Performance and Load Testing](https://www.guru99.com/jmeter-performance-testing.html),
- [How to Run a Stress Test in Jmeter](https://www.blazemeter.com/blog/how-perform-stress-test-jmeter),
- [API Load Testing Best Practices](https://www.soapui.org/learn/load-testing/)

