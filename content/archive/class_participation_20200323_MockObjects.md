title: Class Participation Exercise Mock Objects
date: 2020-03-23
tags: resources, participation, references, practice
authors: Hazel Victoria Campbell
status: published
summary: Individual, Assignments, Participation

---



```
Submit the java code as online text.

// CMPUT 301 Mock Object Quiz!
//
// You probably have to use the back of the page for this quiz.
//
//  WeatherService is a class that gets the weather report from a weather webservice.
//  It parses the webpage and produces a weather report. But sometimes you don't have
//  network conenctivity and sometimes the webservice goes down. Sometimes some
//  locations are not supported by the weather service.
//  Your boss wants you to test against some of these issues.
//
// 1. Write a mock object to enable testing of retrieveWeather.
// 2. Write a testCase using a mock object to ensures that if the weather service page 
//      returns a 404 code error that the LocationException is thrown
// 3. Write a testCase using a mock object to ensures that if the weather service page 
//      returns a 500 server side error code that the NoServiceException is thrown
//
//     Do not modify any of existing code. You may only write NEW code.
class WebserviceException extends Exception { ... }
class LocationException extends WebserviceException { }
class NoServiceException extends WebserviceException { }
class Page { int code; String contents; }
class Weather { ... }
class HTTPGetter {
    Page get(String url) {
        ...
    }
}
class WeatherService {
    HTTPGetter httpGet;
    WeatherService(HTTPGetter getter) { httpGet = getter; }
    protected parseWeather( Page page ) { ... }
    ...
    public Weather retrieveWeather() throws WebserviceException {
         Page page = httpGet.get( this.baseURL + "/” + Location.getCurrentLocation().toString());
         if (page.code == 404) {
             ...
             throw new LocationException("Location not supported!”); // TEST ME!
         } else if (page.code >= 500) {
             ...
             throw new NoServiceException("Service not reachable!”); // TEST ME!
         }
         Weather weather = parseWeather( page );
         return weather;
    }
}

```
