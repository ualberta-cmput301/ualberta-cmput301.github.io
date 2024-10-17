title: Class Participation Exercise Simple Factory
date: 2020-03-27
tags: resources, participation, references, practice
authors: Hazel Victoria Campbell
status: published
summary: Individual, Assignments, Participation

---

**Class Participation Exercise**

Write a Simple Factory that opens a String URI that can either be to:

* a file (starts with file:///),
* a webpage (starts with http://),
* or a TLS/SSL encrypted webpage (starts with https://).

You have the **File** class, the **HTTPFile** class and the HTTPSFile class that all accept a **string** in their constructor giving the **URI** (Uniform Resource Identifier). **HTTPFile** and **HTTPSFile** are subclasses of **File**. Please provide the **code** for the Simple Factory called **FileFactory** that has 1 method:
public File getFile(String str).

BTW Java Strings have a method: public boolean startsWith(String prefix)
