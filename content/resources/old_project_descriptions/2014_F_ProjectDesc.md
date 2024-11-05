Title: 2014 F Project Problem Description             
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2014 F Project Problem Description            
----

You are to design and implement an attractive, usable, interactive Android application to help satisfy the following user's goals. Your design should be flexible enough to allow future developers to extend it to, for example, add new types of entries (see below).


# User's Problem Description
We want a mobile question and answer site. A user can browse questions and post answers. A user can pose questions and see answers. Both question and answers can have a small discussion accompanied with them.

Imagine http://stackoverflow.com/ but geo-location aware.

## Needs in (Partial) User Story Form [do all of these]
User needs are expressed in the form of partial user stories:
as a <role>, I want <goal>
as a <role>, I want <goal> so that <reason>

These descriptions may change to correct omissions and clarify noticed issues.

As a user, I want browse questions.

As a user, I want to view a question and its answers.

As a user, I want to view the replies to a question or answer.

As an author, I want to make questions.

As an author, I want to answer questions by making an answer.

As an author, I want to reply to questions and answers to clarify things.

As an author, I want to attach a picture to my questions or my answers.

As a sysadmin, I do not want the pictures to be large (> 64kb).

As a user, I want to sort questions by if they have pictures.

As a user, I want to sort questions by date or some scoring system.

As a user, I want to upvote the questions of other users.

As a user, I want to upvote the answers of other users

As a user, I want to see the most upvoted questions and most upvoted answers.

As a user, I want to see how many answers a question has received.

As a user, I want to search for questions or answers.

As an author, I want my device to remember which questions I asked.

As a user, I want questions and answers that I read or questions and answers that I've indicated I want to read, to be locally cached so I can read them when I am not on the internet.

As a user, I want to explicitly save some questions as favorites.

As a user, My favorites and their replies should always be available to me regardless of network connectivity.

As an author, I want to author replies, questions and answers offline.

As an author, I want to push my replies, questions and answers online once I get connectivity.

As a user, by default, I should see the most fresh comments.

As an author, I set my username.

## New requirements [Choose 1 of these]
* Requirements Cluster: Geolocation
   - As an author, I want to be asked if my location should be attached to my post
   - As a user I want to be able to query for posts (questions/answers/replies) that are near to me
   - As an author, I want my geolocation to come from my GPS, or allow me to set to it
   - As a user, I want to know if the location of post is near city or town or country.
* Requirements Cluster: Social Analytics
   - As a user, I want to see the trending posts that have recent popularity and activity
   - As a user, I want to see who the top contributors are
   - As a user, I want to see a summary of what topics are trending, that is a textual analysis or summary of what is happening lately
   - As a user, I want to see controversial questions: questions with few upvotes but many replies
   - As a user, I want a word cloud of all the posts cached on my phone.
* Requirements Cluster: Recommendations
   - As a user I want to browse other questions asked by an author
   - As a user I want to browse answers written by an author
   - As an author I want to see related questions when I ask a question
   - As an author I want to see other question I may be able to answer when I write an answer
   - As a user I want to see related questions when I browse questions
* More to come!   

**Notes**

As class advances and questions are asked new story cards will be created.

## Webservice Notes
Please see the URL: http://www.elasticsearch.org/ and Query String DSL

Each group now has its own personal prefix on the elastisearch. Your Android application can communicate to your group's webservice.

Binaries should be small, and you can post them, but be sure you read up on how to send binaries to elastisearch  Core-types , Put Mappings

This webservice is meant to allow posting, listing, deleting and searching recipes. It has a JSON format that can be defined by your group in order to encode more difficult tasks.

http://cmput301.softwareprocess.es:8080/cmput301f14t01/

http://cmput301.softwareprocess.es:8080/cmput301f14t02/

http://cmput301.softwareprocess.es:8080/cmput301f14t03/

http://cmput301.softwareprocess.es:8080/cmput301f14t04/

http://cmput301.softwareprocess.es:8080/cmput301f14t05/

http://cmput301.softwareprocess.es:8080/cmput301f14t06/

http://cmput301.softwareprocess.es:8080/cmput301f14t07/

http://cmput301.softwareprocess.es:8080/cmput301f14t08/

http://cmput301.softwareprocess.es:8080/cmput301f14t09/

http://cmput301.softwareprocess.es:8080/cmput301f14t10/

http://cmput301.softwareprocess.es:8080/cmput301f14t11/

http://cmput301.softwareprocess.es:8080/cmput301f14t12/

http://cmput301.softwareprocess.es:8080/cmput301f14t13/

http://cmput301.softwareprocess.es:8080/cmput301f14t14/

http://cmput301.softwareprocess.es:8080/cmput301f14t15/

http://cmput301.softwareprocess.es:8080/cmput301f14t16/

These are not protected in anyway and they should stick to their own repos.

http://cmput301.softwareprocess.es:8080/testing/ is for testing.


Requirements Cluster: Recommendations
- As a user I want to browse other questions asked by an author
- As a user I want to browse answers written by an author
- As an author I want to see related questions when I ask a question

- As an author I want to see other question I may be able to answer when I write an answer
- As a user I want to see related questions when I browse questions