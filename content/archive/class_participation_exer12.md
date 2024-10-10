Title: Class Participation Exercise 12
date: 2024-09-18
tags: resources, participation, references, practice
authors: Hazel Victoria Campbell
status: published
summary: Individual, Assignments, Participation

----

**Class Participation Exercise 12**


Proper completion of this exercise is considered as part of course participation. An answer will be discussed in class.

You have a design where a two-dimensional rectangle drawing method takes a top left point and a bottom right point. Also, in your design, the points are specified by integer x and y coordinates.

public interface RectangleDrawer {
    public void draw( Point topLeft, Point bottomRight );
}
Suppose, however, you want to reuse a rectangle drawing method that takes four integer parameters: top left x coordinate, top left y coordinate, width, and height.

public class RectangleRenderer {
    public void render( int x, int y, int width, int height ) { ... }
    ...
}
Write Java code for a rectangle drawing object adapter.

public class RectangleDrawerAdapter ...
Submit your Java code as a zip archive.






















