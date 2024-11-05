Title: 2015 F Project Problem Description             
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2015 F Project Problem Description            
----

# Project Problem Description
**Warning: This is subject to change!**
You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the following goals. Your design must be flexible enough to allow developers to extend or migrate it.


<THINGS> will mean the theme of your group project: condiments, sewing tools, tools, craft supplies, baking supplies, kitchen tools, books, DVDs, games, audio equipment, photography equipment, etc. Each team will choose a theme for their app distinct from other teams. TA will approve the theme.


## User's Problem Description
We want to create a distributed library where by we can trade <THINGS> with other people.

We want a mobile application that allows users to record the <THINGS> they have and share them with others! Users can share <THINGS> with each other. This means that you get to see your neighbor's <THINGS> and they can browse your collection of <THINGS>. Then when you want a <THING> from your neighbor you send them a request to see if they want one of your <THINGS> as collateral for their <THING>.

### Needs in (Partial) User Story Form

User needs are expressed in the form of partial user stories:
As a <role>, I want <goal>.
As a <role>, I want <goal> so that <reason>.

These descriptions may change to correct omissions and clarify noticed issues. New requirements will be introduced for the final project part.


### Inventory
US01.01.01

As an owner, I want to remove, edit, or add an item to my inventory that I want to share. It will have a name, quantity, quality, category, if I want to share it with others, and comments.

US01.02.01

As an owner, I want to view my inventory and its details.

US01.03.01

As an owner, I want to view each of my inventory items.

US01.03.01

As an owner, not every item in my inventory will be shared or listed. Items that are not to publicly shared will not be. As an owner, I might use them for trades.

US01.04.01
As an owner, I want to edit and modify inventory items.

US01.05.01
As an owner, I want to delete inventory items.

US01.06.01
As an owner, I want the category for an item to be one of 10 relevant categories for <THINGS>.

US01.07.01
As an owner, I want the entry of an item to have minimal required navigation in the user interface. It must be easy to describe an item.

### Friends
US02.01.01

As an owner, I want to track people I know. Adding a textual username should be enough.

US02.02.01

As an owner, I want to add friends

US02.03.01

As an owner, I want to remove friends

US02.04.01

As an owner or borrower, I will have a profile where by my contact information and city are recorded.

US02.05.01

As an owner or borrower, I will be able to view the profile of anyone I know of including friends.

### Browse Search Inventories of Friends
US03.01.01

As an borrower, I want to search the inventories of my friends.

US03.01.02

As an borrower, I want to search/browse the inventories of my friends by category.

US03.01.03

As an borrower, I want to search/browse the inventories of my friends by textual query..

US03.02.01

As an owner, any of my publicly shared items will be browseable / searchable by my friends.

### Trade with Friends
US04.01.01

As an borrower, I want to offer a trade with a friend. A trade will consist of an item from the owner's inventory and 0 or more items from the borrower's inventory.

US04.02.01

As an owner, when a borrower offers a trade I will be notified of the trade.

US04.03.01

As an owner, I can accept or decline a trade.

US04.04.01

As an owner, upon declining a trade I can offer a counter trade initialized with the items of the declined trade.

US04.05.01

As a borrower or owner, when composing a trade or counter-trade I can edit the trade.

US04.06.01

As a borrower, when composing a trade or counter-trade I can delete the trade

US04.07.01

As an owner, if I accept a trade both parties will be emailed all trade and item information relevant to the trade, as well owner comments for how to continue on with the trade.

US04.08.01

As an owner or borrower, I can browse all past and current trades involving me.

US04.09.01

As an owner or borrower, I can browse all past and current trades involving me as either borrower or owner. I should look at my trades and trades offered to me.

US04.10.01 [must]

As an owner, I can set a trade to complete when the borrower returns the item and the item is now available again.

US04.11.01 [must]

As an owner or borrower, a trade is considered current and in-progress when the item is borrowed.

US04.12.01 [must]

As an owner or borrower, I should be able to browse in-progress trades, and complete trades.

### Photographs of Items
US06.01.01
As an owner, I want to optionally attach photographs of items to the item. Photos are optional for items.

US06.02.01
As an owner, I want to view any attached photograph for an item.

US06.03.01
As an owner, I want to delete any attached photograph receipt on an item, so that unclear images can be re-taken.

US06.04.01
As a sysadmin, I want each receipt image file to be under 65536 bytes in size.

US06.05.01
As a borrower, if photo downloads are disabled, I want the option of manually choosing inventory photos to download.


### Offline Behaviour
US09.01.01
As an owner, I want to make inventory items while offline, and push changes once I get connectivity.

US09.02.01
As a borrower, I want to make trades while offline, and push changes online once I get connectivity.

US09.03.01
As a borrower, I should be able to browse the inventories of friends that I previously looked at. Cache the inventories of the friends.


### Configuration
US10.01.01
As a user, I should be able to specify if I download images or not.

US10.02.01
As a user, I should be to edit my profile.



Your team must choose Option 1 features or Option 2 features and implement them.



### Item Geolocation (Option 1)

US11.01.01

As an owner, I want to have a default geolocation (Lat/Long) that will be assigned to my items.

US11.02.01

As a user, I should be able to search for items near my current location (GPS or Lat/long). E.g. hammers within 2 km.

US11.03.01

As an owner, I should be able use the GPS to determine my geolocation.

US11.04.01

As an owner, I should be able to specifically edit the geolocation of each individual item -- items could be located in different locations.



### Top Traders (Option 2)

US12.01.01

As a user, I should be able to see friends and users who are top-traders. Top traders are users with successful (current, in-progress, and complete) trades. The more successful traders, the more top the trader.

### Item Cloning (Option 2)

US13.01.01

As an owner, I should be able to clone another user's item, if I own it or a copy. E.g. I have the same XBOX game as my friend and I don't want to type it in again.




Revisions:

2015-11-12 - US10 to US13 added, US04.10 to US04.14 added.

2015-10-08 - US09.01.01 and US09.02.01 clarified and editted

2015-10-07 - US06.05.01 changed to manual photo download

2015-10-07 - the trade with friends section had stories renumbered as US.04. (previously US.03.)

2015-10-06 - the last US.06.04.01 becomes US.06.05.01

2015-10-06 - claimant becomes owner in US.06.01.01