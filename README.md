# Web App UI Test Automation

This [repository](https://github.com/ybalenko/WebApp-UI-Test-Automation) contains example scripts and dependencies for running automated **Selenium** [1] UI tests using **Python**. 

In addition, I have also included some samples of using **Sauce Labs** [2] with a common Python test tool (Unittest, in particular).

## To run test samples
>   To run some samples you will need a configuration JSON file (config.json):
>   ```
>   {
>       "saucecreds": {
>           "username": "******",
>           "accessKey": "******"
>       },
>       "imdbcreds": {
>           "email": "******",
>           "password": "******"
>       }
>   }
>   ```


*WHERE*: 
* saucecreds -  [your Sauce Labs User Name and Access Key](https://wiki.saucelabs.com/display/DOCS/Getting+Started)
* imdbcreds - [your IMDb account](https://www.imdb.com/)
### *NOTE*:

1 [Selenium](https://www.selenium.dev/) is a suite of tools for automating web browsers. Selenium WebDriver controls a browser natively, as a real user would, either locally or on remote machines.

2 [Sauce Labs](https://saucelabs.com/) enables running automated web application tests in the Sauce Labs device cloud across multiple operating systems, browsers, and devices.
