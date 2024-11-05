Title: 2013 W Project Problem Description               
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2013 W Project Problem Description              
----

You are to design and implement an attractive, usable, interactive Android application to help satisfy the following user's goals. Your design should be flexible enough to allow future developers to extend it to, for example, add new types of entries (see below).

# User's Problem Description
I want to keep recipes, but I also want to find recipes, eventually I found similar people had similar goals. Some people wanted recipes they could execute immediately given what they had in their fridge or pantry.

I want a system where I can record, post, search and download recipes. I want such a system to be able to address the food I have in my pantry and refridgerator.

It would be nice to include photos of said recipes.

I want the system to query the recipes system with ingredients I already have and have it suggest appropriate recipes.

Furthermore it should be easy to share these recipes over email.

## Needs in (Partial) User Story Form
User needs are expressed in the form of partial user stories:
as a <role>, I want <goal>
as a <role>, I want <goal> so that <reason>

These descriptions may change to correct omissions and clarify noticed issues.

As a user, I want to record recipes.

As a user, I want to share recipes over email.

As a user, I want to publish recipes.

As a user, I want to search for recipes.

As a user, I want to have some recipes cached so that I don't need the internet to work for me to use this program.

As a user, I want to post and publish photos associated with the recipe.

As a user, executing a recipe I want to take photos and attach the photos to the recipe.

As a user, I want the recipes to be stored so I can view them offline.

As a user, recipes I make can have multiple photos.

As a user, I can upload photos for other recipes I did not make, but were downloaded.

As a user, I should be able to retake photos I am taking, if I fail to take the photo I want to correct, so that I don't have erroneous photos.

As a user I should be able to get recipes from other users somehow.

As a user I want to be able to record/edit/view/modify the ingredients I already have.

As a user I want to be able to query for recipes that have the ingredients I already have.

## New requirements

    - As a user, I want to email other users recipes that they can
      immediately import into their recipe program.  [s]


    - As a user, I want to limit modifications of a recipe to myself
      only. -- Note: this doesn't have to be done server side, your
      app could enforce this.  [l]


    - As a user, I want to globally tag recipes. Recipes can have
      multiple tags and other users can see these tags. [l]


    - As a user, I want to browse recipes by tags. [s]


    - As a user, I want to query recipes based on a subset of my
      ingredients. [s]


    - As a user, I want to organize ingredients into folders (like
      fridge, or cabin fridge) and be able to query recipes based on
      these folders. [l]


    - As a user, I want to optionally browse recipes with only photos
      [s]


    - As a user, I want to search recipes I downloaded already. [s]


    - As a user, I want to read/write comments on a recipe. [l]

    - As a user, I want to delete cached recipes (downloaded). [s]


    - As a user, I want to export my recipes to some kind of file so I
      can export them to other programs. [l]

    - As a user, I want to browse the most popular recipes based on their downloaded counts.[l]

    - As a user, I want to STAR good recipes and I want to browse recipes that everyone has given to the most stars. [l]

**Notes**

As class advances and questions are asked new story cards will be created.

## Webservice Notes
Please see the URL: http://www.elasticsearch.org/ and http://www.elasticsearch.org/guide/reference/query-dsl/query-string-query.html

Each group now has its own personal prefix on the elastisearch. Your Android application can communicate to your group's webservice.

Binaries should be small, and you can post them, but be sure you read up on how to send binaries to elastisearch  http://www.elasticsearch.org/guide/reference/mapping/core-types.html http://www.elasticsearch.org/guide/reference/api/admin-indices-put-mapping.html

This webservice is meant to allow posting, listing, deleting and searching recipes. It has a JSON format that can be defined by your group in order to encode more difficult tasks.

http://cmput301.softwareprocess.es:8080/CMPUT301W13T01/

http://cmput301.softwareprocess.es:8080/CMPUT301W13T02/

http://cmput301.softwareprocess.es:8080/CMPUT301W13T03/

http://cmput301.softwareprocess.es:8080/CMPUT301W13T04/

http://cmput301.softwareprocess.es:8080/CMPUT301W13T05/

http://cmput301.softwareprocess.es:8080/CMPUT301W13T07/

http://cmput301.softwareprocess.es:8080/CMPUT301W13T08/

http://cmput301.softwareprocess.es:8080/CMPUT301W13T09/

http://cmput301.softwareprocess.es:8080/CMPUT301W13T10/

http://cmput301.softwareprocess.es:8080/CMPUT301W13T11/

http://cmput301.softwareprocess.es:8080/CMPUT301W13T12/

http://cmput301.softwareprocess.es:8080/CMPUT301W13T13/

http://cmput301.softwareprocess.es:8080/CMPUT301W13T14/


These are not protected in anyway and they should stick to their own repos.

http://cmput301.softwareprocess.es:8080/testing/ is for testing.