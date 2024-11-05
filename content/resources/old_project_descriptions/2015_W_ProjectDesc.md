Title: 2015 W Project Problem Description             
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2015 W Project Problem Description               
----  

# Project Problem Description
**Warning: This is subject to change!**
You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the following goals. Your design must be flexible enough to allow developers to extend or migrate it.

## User's Problem Description
We want a mobile application for travel expense tracking and approval.

### Needs in (Partial) User Story Form

User needs are expressed in the form of partial user stories:
As a <role>, I want <goal>.
As a <role>, I want <goal> so that <reason>.

These descriptions may change to correct omissions and clarify noticed issues. New requirements will be introduced for the final project part.

### Expense Claims / Overall

US01.01.01
As a claimant, I want make an expense claim that records my name, a starting date of travel, and an ending date of travel.

US01.02.01
As a claimant, I want an expense claim to record one or more destinations of travel and an associated reason for travel to each destination.

US01.03.01
As a claimant, I want to view an expense claim and its details.

US01.04.01
As a claimant, I want to edit an expense claim while changes are allowed.

US01.05.01
As a claimant, I want to delete an expense claim while changes are allowed.

US01.06.01
As a claimant, I want entered information to be remembered, so that I do not lose data.

### Expense Claims / Listing

US02.01.01
As a claimant, I want to list all my expense claims, showing for each claim: the starting date of travel, the destination(s) of travel, the claim status, tags, and total currency amounts.

US02.02.01
As a claimant, I want the list of expense claims to be sorted by starting date of travel, in order from most recent to oldest, so that ongoing or recent travel expenses are quickly accessible.

### Expense Claims / Tags

US03.01.01
As a claimant, I want to give an expense claim one or more alphanumeric tags, so that claims can be organized by me into groups.

US03.02.01
As a claimant, I want to manage my personal use of tags by listing the available tags, adding a tag, renaming a tag, and deleting a tag.

US03.03.01
As a claimant, I want to filter the list of expense claims by tags, to show only those claims that have at least one tag matching any of a given set of one or more filter tags.

### Expense Items / Overall

US04.01.01
As a claimant, I want to make one or more expense items for an expense claim, each of which has a date the expense was incurred, a category, a textual description, amount spent, and unit of currency.

US04.02.01
As a claimant, I want the category for an expense item to be one of air fare, ground transport, vehicle rental, private automobile, fuel, parking, registration, accommodation, meal, or supplies.

US04.03.01
As a claimant, I want the currency for an expense amount to be one of CAD, USD, EUR, GBP, CHF, JPY, or CNY.

US04.04.01
As a claimant, I want to manually flag an expense item with an incompleteness indicator, even if all item fields have values, so that I am reminded that the item needs further editing.

US04.05.01
As a claimant, I want to view an expense item and its details.

US04.06.01
As a claimant, I want to edit an expense item while changes are allowed.

US04.07.01
As a claimant, I want to delete an expense item while changes are allowed.

US04.08.01
As a claimant, I want the entry of an expense item to have minimal required navigation in the user interface.

### Expense Items / Listing

US05.01.01
As a claimant, I want to list all the expense items for a claim, in order of entry, showing for each expense item: the date the expense was incurred, the category, the textual description, amount spent, unit of currency, whether there is a photographic receipt, and incompleteness indicator.

### Expense Items / Receipts

US06.01.01
As a claimant, I want to optionally take a single photograph of a receipt and attach the photograph to an editable expense item, so that there is supporting documentation for the expense item in case the physical receipt is lost.

US06.02.01
As a claimant, I want to view any attached photographic receipt for an expense item.

US06.03.01
As a claimant, I want to delete any attached photographic receipt on an editable expense item, so that unclear images can be re-taken.

US06.04.01
As a sysadmin, I want each receipt image file to be under 65536 bytes in size.

### Expense Claims / Statuses

US07.01.01
As a claimant, I want to submit an expense claim for approval, denoting the claim status as submitted, with no further changes allowed by me to the claim information (except the tags).

US07.02.01
As a claimant, I want a visual warning when trying to submit an expense claim when there are fields with missing values or there are any incompleteness indicators on the expense items.

US07.03.01
As a claimant, I want a submitted expense claim that was not approved to be denoted by a claim status of returned, with further changes allowed by me to the claim information.

US07.04.01
As a claimant, I want a submitted expense claim that was approved to be denoted by a claim status of approved, with no further changes allowed by me to the claim information (except the tags).

US07.05.01
As a claimant, I want to see the name of the approver and any comment(s) from the approver on a returned or approved claim.

### Expense Claims / Approval

US08.01.01
As an approver, I want to view a list of all the expense claims that were submitted for approval, which have their claim status as submitted, showing for each claim: the claimant name, the starting date of travel, the destination(s) of travel, the claim status, total currency amounts, and any approver name.

US08.02.01
As an approver, I want the list of submitted expense claims to be sorted by starting date of travel, in order from oldest to most recent, so that older claims are considered first.

US08.03.01
As an approver, I want to view all the details of a submitted expense claim.

US08.04.01
As an approver, I want to list all the expense items for a submitted claim, in order of entry, showing for each expense item: the date the expense was incurred, the category, the textual description, amount spent, unit of currency, and whether there is a photographic receipt.

US08.05.01
As an approver, I want to view any attached photographic receipt for an expense item.

US08.06.01
As an approver, I want to add a comment to a submitted expense claim, so that I can explain why the claim was returned or provide accounting details for a payment.

US08.07.01
As an approver, I want to return a submitted expense claim that was not approved, denoting the claim status as returned and setting my name as the approver for the expense claim.

US08.08.01
As an approver, I want to approve a submitted expense claim that was approved, denoting the claim status as approved and setting my name as the approver for the expense claim.

### Expense Claims / Offline

US09.01.01
As a claimant, I want to make and work on expense claims and items while offline, and push application and expense information online once I get connectivity.