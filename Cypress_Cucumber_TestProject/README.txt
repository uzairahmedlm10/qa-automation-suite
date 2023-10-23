Project : Cypress Cucumber Framework (JavaScript)

Description:
In this project, we utilize the Cypress Cucumber framework to automate testing for various web applications. These test scripts are built with the Page Object Design pattern for efficient maintenance and execution.

Project Structure:
Cypress_Cucumber_TestProject: The directory for the Cypress Cucumber framework project.

- fixtures/example: This contains the test data that is fed to the test cases via fixtures.  
- Integration/BDD: This folder contains subdirectories, each dedicated to testing scripts for different web applications, all organized using fixtures and the Page Object Design pattern:
      - RegistrationForm: Functional test cases for a registration page on an e-commerce website.
      - Veg Delivery: Functional test scripts for another e-commerce website.
      - Ecommerce: Functional test cases of another shopping website.
      - API_BookLibrary: Test cases that include API calls, mocking API requests, and responses for an e-library.
      - PageObjects: All the page object classes can be found in this folder.
  

Additional Information
For Cypress Cucumber test scripts, it is possible to connect with the Cypress Cloud to access and review logs for test executions. 