Title: Class Participation Exercise Proxy Pattern
date: 2024-09-18
tags: resources, participation, references, practice
authors: Jakaria Rabbi
status: published
summary: Individual, Assignments, Participation

----

**Class Participation Exercise: Proxy Pattern**

Use the Proxy pattern to improve performance by not reading files that aren't actually needed yet.

```.java
interface OurFile {
    byte[] fileContents(); // returns entire file
    String getName();
}
class ConcreteFile implements OurFile {
    String name;
    byte[] fileContents;
    ConcreteFile(String name) { ... }
    String getName() { return name; }
    byte[] fileContents() { return fileContents; }
    ...
}
```

assume ```ConcreteFile``` exists and implements ```OurFile```. ```ConcreteFile``` reads the entire file when it is constructed.

Write java code for ```ProxyFile``` that proxies a ```ConcreteFile``` and doesn't have to read the entire file until  the contents of the file are needed, using the proxy pattern.