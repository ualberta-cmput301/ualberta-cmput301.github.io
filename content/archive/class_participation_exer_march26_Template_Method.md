Title: Class Participation Exercise: Template Method Pattern (Mar 26)  
date: 2024-09-19    
tags: resources, reading, references, practice  
authors: Hazel Victoria Campbell, Tina Nguyen  
status: published  
summary: Individual, Assignments, Participation  

----

**Class Participation Exercise: Template Method Pattern**

Rewrite `countWords()`
* Convert the `countWords()` method to a template method using the **Template Method Pattern**, removing the conditionals.

Write code for one of the following subclasses:
* `RawWordCounter`
* `WordCounterNoStopWords`
* `LowerCaseWordCounter`

```java
public class WordCounter {
...
void countWords() {
    loadData();
    if (lowerCaseWords) {
        lowerCaseData();
    }
    if (removeStopWords) {
        filterStopWords();
    }
    calculateTermFrequency();
    calculateTermDocumentFrequency();
    saveCountData();
}
}
```
