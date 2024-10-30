Speaker is a class that utters words and uses the **state** pattern to change its behaviour.

```java

class Speaker {

    Speak speak;

   // delegate behaviour

   public String speak() {

       return speak.speak();

    }

     ...

}

public interface Speak {

     public String speak();

}

class Squawk implements Speak { ... }

class Cluck implements Speak { ... }

class Tick implements Speak {

     public String speak() {

          return "Tick”;

     }

}
```

Speaker has behaviours such as Squawk which returns random Squawking strings, and Cluck which returns random clucking strings. Tick just returns "Tick”.

**Finish** this decorator for Speak states that lowercases the Speak states.

```java
//"X”.toLowerCase().equals("x”)

class LowerCaseSpeakDecorator implements Speak {

     Speak speak;

     LowerCaseSpeakDecorator(Speak delegate) {

         speak = delegate;

     }

     public String speak() {







     }

}
```

Show how to make a lowercase tick behaviour.
