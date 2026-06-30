Title: Lab 3 Instructions
date: 2026-06-30
tags: labs, policy, grading
authors: Raj Prasad, Michelle Deng
status: published
summary: Lab 3 Instructions

----

[TOC]


# Lab 3: More Android  

## 1. Getting Started

1. Clone this repository and open the `/code` folder in Android Studio.
2. You'll find a basic `ListyCity` app that displays a static list of cities and provinces.

## 2. Demo Instructions

During the lab demo, we'll implement "Add City" functionality:

1. Review [Lab 3 Slides](https://ualberta-cmput301.github.io/labs/slides/Lab_3_Slides_2026.pdf)
2. Follow along with [Lab 3 Instructions](https://ualberta-cmput301.github.io/labs/slides/Lab_3_Instructions_2026.pdf)
3. Read about Code Conventions (see the [Kotlin Code Conventions PDF](https://ualberta-cmput301.github.io/labs/slides/Kotlin_Code_Conventions.pdf)).
4. By the end, you'll have implemented the ability to add new cities to the list.

## 3. Lab 3 Participation Exercise

### Task

- Add functionality to `ListyCity` to allow **editing** existing cities. The design implementation is flexible and up to your creativity.
- Update the `README.md` and the `LICENSE.md` with your details.

### Example Implementation

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
    <img src="assets/img1.png" width="300" style="margin: 20px;">
    <img src="assets/img2.png" width="300" style="margin: 20px;">
    <img src="assets/img3.png" width="300" style="margin: 20px;">
    <img src="assets/img4.png" width="300" style="margin: 20px;">

</div>

<br>

> **Note:** Your app does NOT need to look exactly like the screenshots.  The only requirement is the ability to edit an existing city.  

## 4. Implementation Tips

### 1. City Class Updates

- The starter code uses a `City` data class with `val` properties:

```kotlin
data class City(
    val name: String,
    val province: String
)
```

Since name and province use val, they cannot be changed directly after a City object is created

To edit a city, create a new City object with the updated values and replace the old city in the list

Example:
```kotlin
val updatedCity = City(
    name = newCityName,
    province = newProvinceName
)
```

### 2. Choose Your Implementation

Recommended Approach:

- Track which City object is selected
- Store the edited city name and province in text fields
- Create a new City object with the updated values
- Replace the selected city in the list


### Example Code

One approach is to add an updateCity() function to CityRepository:

```kotlin
fun updateCity(oldCity: City, updatedCity: City) {
    val index = _cities.indexOf(oldCity)
    if (index != -1) {
        _cities[index] = updatedCity
    }
}
```

### Compose Hints

- Use state to track the selected city:
```kotlin
var selectedCity by remember { mutableStateOf<City?>(null) }
```

- A city row can be made selectable using Modifier.clickable { ... }
- Text fields can be reused to enter the updated city name and province
- Use a callback such as onUpdateCity(oldCity, updatedCity) to send the edit action upward


## 5. Submission

> [!CAUTION]
> Make sure to commit **and** push your code to the GitHub repository before the deadline!
> 
> Once you completed, please go to [Canvas](https://canvas.ualberta.ca/) and submit **your Lab 3 GitHub repository link**.