Proper completion of this exercise is considered as part of course participation.

Which of these code smells are signs of "bloat", i.e., code, methods, and classes that have increased to an extent that they become hard to work with.
- comments
- duplicated code
- long method
- large class
- data classes
- data clumps
- large parameter list
- divergent change
- shotgun surgery
- feature envy
- inappropriate intimacy
- message chains
- primitive obsession
- switch statements
- speculative generality
- refused bequest

Which of these code smells are signs of incomplete or incorrect use of object-oriented design principles?
- comments
- duplicated code
- long method
- large class
- data classes
- data clumps
- large parameter list
- divergent change
- shotgun surgery
- feature envy
- inappropriate intimacy
- message chains
- primitive obsession
- switch statements
- speculative generality
- refused bequest

Which of these code smells are signs that change is difficult and likely expensive?
- comments
- duplicated code
- long method
- large class
- data classes
- data clumps
- large parameter list
- divergent change
- shotgun surgery
- feature envy
- inappropriate intimacy
- message chains
- primitive obsession
- switch statements
- speculative generality
- refused bequest

Which of these code smells are signs of something unnecessary, which if avoided would lead to cleaner, more efficient, and easier to understand code?
- comments
- duplicated code
- long method
- large class
- data classes
- data clumps
- large parameter list
- divergent change
- shotgun surgery
- feature envy
- inappropriate intimacy
- message chains
- primitive obsession
- switch statements
- speculative generality
- refused bequest

Which of these code smells are signs of excessive coupling between classes?
- comments
- duplicated code
- long method
- large class
- data classes
- data clumps
- large parameter list
- divergent change
- shotgun surgery
- feature envy
- inappropriate intimacy
- message chains
- primitive obsession
- switch statements
- speculative generality
- refused bequest

Consider the following piece of code:
```java
// Order.java

package com.nq.util;
 
import java.io.*;
import java.util.*;
import java.lang.*;
 
public class Order {
 
    private lineitemlist lineItemList;
 
    public Order(lineitemlist lis) {
        lineItemList = lis;
    }
 
    public boolean equals(Object aThat) {
            if ( this == aThat ) return true;
        if ( !(aThat instanceof Order) ) return false;
            Order that = (Order)aThat;
        return this.lineItemList.equals(that.lineItemList);
    }
 
    // writes this order object to the specified print writer
    public void writeOrder(Order order, PrintWriter pw) {
        // get a vector of line items
        Vector lineItems = order.getLineItemList().getLineItems();
 
        // ------------------------------------------------------
        // calculate total
        // ------------------------------------------------------
        // create an iterator for the vector
        Iterator iter = lineItems.iterator();
        lineItem item;
        // set total to zero
        int total = 0;
            while (iter.hasNext()) {
                item = (lineItem)iter.next();
 
                // calculate total for line item
                int unitPrice = item.getUnitPrice();
                int qty = item.getQuantity();
                int lineitemtotal = unitPrice * qty;
 
                total += lineitemtotal;
            }
        // ------------------------------------------------------
        // END calculate total
        // ------------------------------------------------------
 
        // ------------------------------------------------------
        // write order
        // ------------------------------------------------------
        // create an iterator for the vector
        iter = lineItems.iterator();
            while (iter.hasNext()) {
                item = (lineItem)iter.next();
 
                // calculate total for line item
                int unitPrice = item.getUnitPrice();
                int qty = item.getQuantity();
                int productID = item.getProductID();
                int imageID = item.getImageId();
                int lineitemtotal = unitPrice * qty;
 
                pw.println("Begin Line Item");
                pw.println("Product = " + productID);
                pw.println("Image = " + imageID);
                pw.println("Quantity = " + qty);
                pw.println("Total = " + lineitemtotal);
                pw.println("End Line Item");
            }
        pw.println("Order total = " + total);
    }
 
    public int getTotal() {
        // get a vector of line items
        Vector lineItems = lineItemList.getLineItems();
        // create an iterator for the vector
        Iterator iter = lineItems.iterator();
        lineItem item;
        // set total to zero
        int total = 0;
            while (iter.hasNext()) {
                item = (lineItem)iterator.next();
 
                // calculate total for line item
                int unitPrice = item.getUnitPrice();
                int qty = item.getQuantity();
                int lineitemtotal = unitPrice * qty;
 
                total += lineitemtotal;
            }
            return total;
    }
}
 
// lineitemlist.java

package com.nq.util;
 
import java.io.*;
import java.util.*;
import java.lang.*;
 
class lineitemlist {
    private Vector LIList;
 
    public void setLineItems(Vector lineItems) {
        LIList = lineItems;
    }
 
    Vector getLineItems() {
        return LIList;
    }
}

// lineItem.java

package com.nq.util;
 
import java.io.*;
import java.util.*;
import java.lang.*;
 
class lineItem {
    protected int productId;
    private int ImageID;
    private int qty;
    private int Unitprice;
 
    public lineItem(int prodID, int ImageID, int inQty) {
        productId = prodID;
        this.ImageID = ImageID;
        qty = inQty;
    }
 
    public void setLineItems(Vector lineItems) {
        LineItems = lineItems;
    }
 
    Vector getLineItems() {
        return LineItems;
    }
 
    int getProductID() {
        return productId;
    }
 
    int getImageID() {
        return imageID;
    }
 
    int getQuantity() {
        return qty;
    }
 
    int getUnitPrice() {
        return Unitprice;
    }
 
    public void setProductID(int id) {
        productId = id;
    }
 
    public void setImageID(int ID) {
        imageID = ID;
    }
 
    public void setQty(int qty) {
        this.qty = qty;
    }
 
    public void setUnitPrice(int i) {
        Unitprice = i;
    }
}
```

What code smells are evident? For each, briefly describe its occurrence(s) in the code.

Occurrence(s) of "comments" code smell: <br>

Occurrence(s) of "duplicated code" code smell:<br>

Occurrence(s) of "long method" code smell:<br>

Occurrence(s) of "large class" code smell:<br>

Occurrence(s) of "data classes" code smell:<br>

Occurrence(s) of "data clumps" code smell:<br>

Occurrence(s) of "large parameter list" code smell:<br>

Occurrence(s) of "divergent change" code smell:<br>

Occurrence(s) of "shotgun surgery" code smell:<br>

Occurrence(s) of "feature envy" code smell:<br>

Occurrence(s) of "inappropriate intimacy" code smell:<br>

Occurrence(s) of "message chains" code smell:<br>

Occurrence(s) of "primitive obsession" code smell:<br>

Occurrence(s) of "switch statements" code smell:<br>

Occurrence(s) of "speculative generality" code smell:<br>

Occurrence(s) of "refused bequest" code smell:<br>

Other occurrence(s) of inconsistent or nonstandard coding:<br>
