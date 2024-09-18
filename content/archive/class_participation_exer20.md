Title: Class Participation Exercise 20
date: 2024-09-10
tags: resources, participation, references, practice
authors: Hazel Victoria Campbell
status: published
summary: Individual, Assignments, Participation

----

**Class Participation Exercise 20**

Consider the following method to compute the base-two logarithm of a byte value (assumed positive here, maximum 127), truncated down to the nearest integer. For example, if the byte value is 17, the method returns 4.

```.java
public static int logb2( byte b ) {
    return (int)( Math.log( b ) / Math.log( 2 ) );
}
```

Assume this method is heavily used, and that operations like Math.log( double ) are relatively slow and should be avoided.

Optimize this method to reduce the computation time needed, while maintaining the same expected behavior and using comparable data space. Your method must be proper Java and be a self-contained implementation (not call other methods). Add comments as appropriate to explain how it is intended to work.
