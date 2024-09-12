Title: participation 15
date: 2024-09-12
tags: resources, reading, references, practice
authors: Ildar Akhmetov
status: published
summary: Individual, Assignments, Participation

----

**Class Participation Exercise 15**

Proper completion of this exercise is considered as part of course participation. An answer will be discussed in class.

Consider the following (partial) implementation of a Person class.

```.java
class Person {
    …

    public String getName() {
        return name;
    }

    public String getTelephoneNumber() {
        return “(“ + officeAreaCode + “) “ + officeNumber;
    }

    String getOfficeAreaCode() {
        return officeAreaCode;
    }

    void setOfficeAreaCode( String areaCode ) {
        officeAreaCode = areaCode;
    }

    String getOfficeNumber() {
        return officeNumber;
    }

    void setOfficeNumber( String number ) {
        officeNumber = number;
    }

    private String name;
    private String officeAreaCode;
    private String officeNumber;
}
```

Draw the UML class diagram for the refactored design.

Submit your diagram as a PNG file.
