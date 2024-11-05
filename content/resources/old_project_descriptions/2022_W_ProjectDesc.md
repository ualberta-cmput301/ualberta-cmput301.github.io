Title: 2022 W Project Problem Description    
date: 2024-11-04    
tags: projects, teams, grading  
authors: Tina Nguyen, Hazel Victoria Campbell  
status: published
summary: 2022 W Project Problem Description  
----

# Project Problem Description
Warning: This is subject to change!

You are to design and implement a simple, attractive, and easy-to-use Android application to satisfy the following goals. Your design must be flexible enough to allow developers to extend or migrate it.

We want a mobile application that allows us to hunt for the coolest QR codes that score the most points. Players will run around scanning QR codes, barcodes, etc. trying to find barcodes and QR codes that give them the most points.

QR codes and barcodes (scannable codes) will be hashed and the hashes they produce will be analyzed and scored. A QR code that has certain properties like repeated nibbles or bytes (hex digits) will have a higher score than a QR code that does not. We have a proposed scoring system, but the implementers are free to use a different scoring system.

We want users to compete with each other for the highest scoring QR codes, the most QR codes, the highest sum of QR codes, or highest scoring QR codes in a region. 

When a player scans a QR code they will take a photo of what or where the QR code is and also record the geolocation of the QR code. 

Players can see on a map local QR codes that other players have scanned.

## Scenario:
I open my QRHunter app. I see a QR code in my wallet. I indicate I want to add a new QR code and I use the phone camera to add the QR code. The QR code is scored and I’m told that my QR score is 30. The system prompts me for a photo of the object I scanned. I decline since this was an ID card. I also decline geolocation because it is in my wallet. The system adds the 30 points to my total score and records a hash of the QR code. I then see some sticker on a pole. I scan it and am told it is worth 1000 points! I record the geolocation and take a photo of the pole and save it to my account. 1000 points wow. Then I see that other users have found this pole as well. So I open the map for nearby QR codes and I see something worth 10000 is 100 meters away so I’m going to head on over there!

<br>
<br>

## Needs in (Partial) User Story Form
#### Actors:

Player: a person who plays the game

Owner: the entity that owns the infrastructure that the game runs on.

#### Glossary:

QR Code: a scannable code, either a barcode, a QR code, or other code scannable by Zebra crossing libraries or google QR code scanning libraries.

User needs are expressed in the form of partial user stories:

As a <role>, I want <goal>.

These descriptions may change to correct omissions and clarify noticed issues. New requirements will be introduced for the final project part.

#### Player

US 01.01.01

As a player, I want to add new QR codes to my account.

US 01.02.01

As a player, I want to see what QR codes I have added to my account.

US 01.0X.01

As a player, I want to remove QR codes from my account.

US 01.0X.01

As a player, I want to see my highest and lowest scoring QR codes.

US 01.0X.01

As a player, I want to see the sum of scores of QR codes that I have scanned.

US 01.0X.01

As a player, I want to see the total number of QR codes that I have scanned.

US 01.0X.01

As a player, I want to see other player’s profiles

#### Game QR Codes

US 02.0X.01

As a player, I want to be able to scan QR codes and record a photo of the location or object, and the geolocation of the location or object.

US 02.0X.01

As a player, I want to be able to comment on QR codes.

US 02.0X.01

As a player, I want to be able to browse QR codes that I own. (2022-03-08: Deleted because identical to US 01.02.01)

US 02.0X.01

As a player, I want to be able to browse QR codes that other players have scanned.

US 02.0X.01

As a player, I want to see that other players have scanned the same QR code.


#### Player QR Codes

US 03.0X.01

As a player, I want to be able to generate QR codes so that other players can scan my QR code to see my game status.

US 03.0X.01

As a player, I want to be able to generate a QR code so that I can log in to another device with the same account. 


#### Player profile

US 04.01.01

As a player, I want a profile with a unique username and my contact information.

US 04.0X.01 

As a player, I do not want to log into my application using a username and password as my device can identify me.


#### Searching

US 05.01.01

As a player, I want to search for other players by username.

US 05.0X.01

As a player, I want to search for nearby QR codes by using geolocation.


#### Location

US 06.01.01

As a player, I want to see a map of geo-locations of nearby QR codes.


#### Scoring

US 07.0X.01

As a player, I want to see game-wide high scores of all players.

US 07.0X.01

As a player, I want an estimate of my ranking for the highest scoring unique QR code.

US 07.0X.01

As a player, I want an estimate of my ranking for the total number of QR codes scanned.

US 07.0X.01

As a player, I want an estimate of my ranking for a total sum of scores of QR codes scanned.


#### Privacy

US 08.0X.01

As a player, I don’t want the actual code recorded. E.g., so I can scan and score my vaccine passport.

US 08.0X.01

As a player, I want to be able to decline recording geolocation for privacy reasons.


#### Owner

US 09.0X.01 

As an owner, I don’t want to store big images online.

US 09.0X.01 

As an owner, I want to be able to delete QR codes that are bad or malicious.

US 09.0X.01 

As an owner, I want to be able to delete players.



## Proposed Scoring System:

First, we calculate a SHA-256 hash of the QR code contents.

Example:

QR code contents: **BFG5DGW54**

Calculating SHA-256 hash:

@slate:~$ echo BFG5DGW54 | sha256sum
696ce4dbd7bb57cbfe58b64f530f428b74999cb37e2ee60980490cd9552de3a6  -

Then, based on the hexadecimal representation of the sha256, the score is calculated in the following way:

a "0" is 1 point

Many 0 in a row are multiplied by 20^(n-1) whereby n is the number of repeats

00 - 20^1 - 20

000 - 20^2 - 400

0000 - 20^3 - 8000

Same for other numbers

11 - 1

111 - 1

1111 - 1

22 - 2

222 - 4

2222 - 8

99 - 9

999 - 81

aa - 10

aaa - 100

ff - 15

fff - 225

So the best QR code would be made of all 0s or higher digits


For the QR code above

**696ce4dbd7bb57cbfe58b64f530f428b74999cb37e2ee60980490cd9552de3a6**

Let’s find the repeated digits

echo BFG5DGW54 | sha256sum | perl -lpe 'print "$1$2" while /([0-9a-f])(\1+)/g'

bb
999
ee
55

And calculate the score

bb - 11

999 - 9^2 - 81

ee - 14

55 - 5

Score: 11 + 81 + 14 + 5 = 111


### Changelog:
2022-03-08: Deleted US 02.0X.01 ("As a player, I want to be able to browse QR codes that I own"). Reason: identical to US 01.02.01.