Title: Practice Midterm W23 Q1
date: 2024-09-11
tags: resources, reading, references, practice, exams
authors: Ildar Akhmetov
status: published
summary: Practice Exam Question

----

Convert this Java code to a UML class diagram. This Java code is meant to represent a hospital. Draw a well-designed UML class diagram to represent this information. Provide the basic abstractions, attributes, methods, relationships, multiplicities, and navigabilities as appropriate.
"..." means much code is omitted.

```.java
class Animal {
    protected String name;
    protected int age;
    public String getName() { return name; }
}

interface Predator {
    public boolean hunt(Animal a);
}

interface Herbivore {
    public void eat(Plant p);
}

class Lion extends Animal implements Predator {
    public boolean hunt(Animal a) {
        // ...
    }
    // ...
}

class Zebra extends Animal implements Herbivore {
    protected int stripes;
    public void eat(Plant p) {
        // ...
    }
}

class Savannah {
    private int area;
    private Lion alphaLion;
    protected ArrayList<Animal> inhabitants = new ArrayList<Animal>();
}
```
