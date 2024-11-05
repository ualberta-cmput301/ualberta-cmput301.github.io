Title: 2011 W Project Problem Description               
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2011 W Project Problem Description              
----

# Project Problem Description
You are to design and implement an attractive, usable, interactive Java application to help satisfy the following user's goals. Your design should be flexible enough to allow future developers to add new types of entries (see below).

## Needs In (Partial) User Story Form
These needs are expressed in the form of partial user stories:
as a <role>, I want <goal>
as a <role>, I want <goal> so that <reason>

These description may change in minor ways to correct omissions and clarify noticed issues.


- As a user, I want to keep a record of my daily fitness-related activities in a journal so that I can monitor my progress. Types of entries include cardio workouts (i.e., outdoor cycling), strength workouts (i.e., free weights), and comment. There may be multiple, reorderable entries per day.


- As a user, I want to see the entries for a single day, and move backwards and forwards one day at a time.


- As a user, I want to see the entries for the days of four weeks at a time, and move backwards and forwards one week at a time. A week begins on Monday and ends on Sunday.


- As a user, I want to be able to add, edit, and delete entries, including instant, multiple undo and redo of these changes (at the level of entries), so that I can freely make changes at any time.


- As a user, I want data entry to be quick and structured, yet not unduly fussy. This is especially important if I happen to be using the application during a strength workout to keep track of exercises.


- As a user, I want to obtain help, so that I can learn what tasks I can do and what a data field is intended for.


- As a user, I want a comment entry to record a non-workout activity or general observation. Typical uses would be, for example, to note a meal, a weight measure, a waist measure, a resting heart rate measure, a soreness, a sickness, fatigue, mood, etc.


- As a user, I want each outdoor cycling workout to include the following information: trip distance (in km, to 2 decimal places), trip time (in hh:mm:ss format), average speed (in km/h, to 2 decimal places), average cadence (in whole revolutions/min), and maximum speed (in km/h, to 2 decimal places). This data will be entered manually, in that order.


- As a user, I want each outdoor cycling workout to include the following optional weather-related information: temperature (in whole degrees Celsius), wind speed (in whole km/h), and direction (one of 16 compass points). This data will be entered manually, in that order.


- As a user, I want each cardio workout to include the following information: time in zone (in hh:mm:ss format), zone start (in whole beats/min), zone end (in whole beats/min), average heart rate (in whole beats/min), peak heart rate (in whole beats/min), and calories expended (in whole kcal). This data will be entered manually, in that order.


- As a user, I want to name and specify preset heart rate values of up to 5 heart rate zones, so that I can choose a named zone to quickly fill in the values for the zone start and end in a cardio workout.


- As a user, I want each free-weight workout to include for each exercise, the exercise name (required), number of sets (optional), number of reps (optional), and amount of weight (optional).


- As a user, I want each strength workout to include the time duration in hh:mm.


- As a user, I want to specify a workout in advance to remind me what activity to do on a particular day. I can delete the workout should it not occur.


- As a user, I want to have a plan for a workout, detailing a particular goal or set of exercises. After the workout, I can rate the workout (0 to 5) on how well I achieved that goal or completed the exercises.


- As a user, I want to avoid reentering plan details if different workouts will have the same plan. Also plans for different workout types should not be mixed.


- As a user, I want to add a free-form note to a workout, containing anything else that doesn't belong to one of the existing data fields.


- As a user, I want to have a brief free-form note for a week, so that I can specify the cardio and/or strength goal or phase for that week.


- As a user, I want to see (as needed) a chart of outdoor cycling total trip distances covered in each month for a given year and previous year compared. It should be possible to have this chart visible as workouts are edited. If there is no data for a particular year, omit that year.


- As a user, I want to see (as needed) a chart of outdoor cycling total trip times done in each month for a given year and previous year compared. It should be possible to have this chart visible as workouts are edited. If there is no data for a particular year, omit that year.


- As a user, I want to see the outdoor cycling total trip distance covered and total trip time done so far in the current year compared to that of the previous year.