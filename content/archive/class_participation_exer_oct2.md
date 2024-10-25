Title: A1/A2 2nd October Class Exercise  
date: 2024-10-17  
tags: resources, reading, references, practice  
authors: Hazel Victoria Campbell, Tina Nguyen  
status: published  
summary: Individual, Assignments, Participation  

----

**Class Participation Exercise Oct 2**

The Java code below is software for a tiny sound recorder used by spies. It has a physical hardware counter display to show how much recording time is left and a button that starts it recording and stops it.  
Refactor/Restructure this single class into MVC classes as a UML diagram. You do not need to diagram the original code, you only need to make a UML class diagram for your new MVC version of the code. Only refactor the code shown. You do not need to include the TimeCounter or Microphone classes in your UML, because they are static hardware that you cannot change or reprogram.  
On the diagram, clearly label which classes represent model, view, and controller. Your UML class diagram should have all the basic abstractions, attributes, methods, relationships, multiplicities, and navigabilities as appropriate. “...” means much code is omitted.  
Use the “active model” type of MVC that we discussed in class: the one that uses the observer pattern.  
Do not submit Java, submit UML.

<br>

```java
public class SpyCorder {
    final int storage;
    private boolean enabled;
    private ArrayList<Sounds> recording;

    SpyCorder(int storage) {
        this.storage = storage;
        enabled = false;
        runLoop();
    }

    void runLoop() {
        while (true) {
            if (enabled) {
                recording.add(Microphone.listen());
            }
            showRemaining();
        }
    }

    void buttonPressed() {
        enabled = !enabled;
    }

    void showRemaining() {
        TimeCounter.show(storage - recording.size());
    }
}
```

<br>

**Add your name and your partner's name (if you have one) to the diagram. If you don't, you won't get credit.**

Upload a screenshot. If you worked in a pair, get the screenshot from your partner and upload the same screenshot.

You can screenshot a diagrammer of your choice, or draw it on paper and take a photo.
Here's a handy diagrammer online: https://app.diagrams.net/ IF that one doesn't work for you, try a different one.
