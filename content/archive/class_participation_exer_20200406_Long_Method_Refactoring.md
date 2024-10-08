Title: Class Participation Exercise 2020-04-06 Long Method Refactoring
date: 2024-09-17    
tags: resources, reading, references, practice  
authors: Hazel Victoria Campbell, Tina Nguyen  
status: published  
summary: Individual, Assignments, Participation  

----
**Class Participation Exercise: Long Method Refactoring**

Extracts methods from this long method body by putting a box around code that will go into a new method. Then on the right hand side of that box write the method name.

At the bottom, rewrite insertRecipe using those new methods.

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