# Class Participation Exercise: Template Method Pattern (Mar 26)

**Date:** 2024-09-19  
**Tags:** resources, reading, references, practice  
**Authors:** Hazel Victoria Campbell, Tina Nguyen  
**Status:** published  
**Summary:** Individual, Assignments, Participation

----

## Problem

### 1. Rewrite `countWords()`
- Convert the `countWords()` method to a template method using the **Template Method Pattern**, removing the conditionals.

### 2. Write code for one of the following subclasses:
- `RawWordCounter`
- `WordCounterNoStopWords`
- `LowerCaseWordCounter`

----

### Code

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
