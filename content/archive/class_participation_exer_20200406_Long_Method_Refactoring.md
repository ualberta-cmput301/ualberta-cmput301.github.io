# Class Participation Exercise 2020-04-06 Long Method Refactoring

**Date:** 2024-09-17  
**Tags:** resources, reading, references, practice  
**Authors:** Hazel Victoria Campbell
**Status:** published  
**Summary:** Individual, Assignments, Participation

----

## Instructions

1. Extracts methods from this long method body by putting a box around code that will go into a new method. Then on the right hand side of that box write the method name.
2. At the bottom, rewrite insertRecipe using those new methods.

---

##Code 

```.java
/**

* Inserts a Recipe into the Webservice

*/

public void insertRecipe(Recipe recipe){

     StringEntity stringentity = null;

     try {

         stringentity = new StringEntity(gson.toJson(recipe));

     } catch (UnsupportedEncodingException e) {

          handleError(e);

     }

     HttpPost httpPost = new HttpPost(recipeURI);

     httpPost.setHeader("Accept","application/json");

     httpPost.setEntity(stringentity);

     HttpResponse response = null;

     try {

          response = httpclient.execute(httpPost);

     } catch (ClientProtocolException e) {

          handleError(e);

     } catch (IOException e) {

          handleError(e);

     }

      HttpEntity entity = response.getEntity();

      try {

          EntityUtils.consume(entity);

     } catch (IOException e) {

         handleError(e);

     }

     httpPost.releaseConnection();

}

public void insertRecipe(Recipe recipe) { // your new refactored method

}
```