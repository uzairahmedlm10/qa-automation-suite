This repository contains two projects for quality assurance (QA) web applications automation testing. 

Project 1: Selenium Webdriver with Pytest (Python)

Description:
In this project, we focus on automated testing of an e-commerce website using Selenium Webdriver and the Pytest framework. The tests are organized using the Page Object Design pattern for better code organization and maintenance.

Project Structure:

Selenium_Pytest_Framework: The core directory for the Selenium Webdriver and Pytest framework project.
  - TestCases: This folder contains functional test scripts for an e-commerce website.
  - PageObjects: All page object classes that facilitate the framework are stored in this folder.
  - Utility: This folder contains the utility base classes for the respective websites. These classes are being inherited in   the actual test cases.
  - TestData: This contains the data that is fed to the test cases via fixtures.

TestCases:
- SearchProducts.py: This file contains functional test cases related to the e-commerce website. Test scenarios are documented within comments, and the script makes use of fixtures and a base class streamlined test execution.
- VerifyOTP.py: This test file automates the process of user registration on the 'Hubspots' website. It integrates with a Gmail server to extract a One-Time Password (OTP) and activate the account on Hubspot. Like other scripts, it uses fixtures and inherits from a base class to ensure efficient test execution.

Project 2: Cypress Cucumber Framework (JavaScript)

Description:
In this project, we utilize the Cypress Cucumber framework to automate testing for various web applications. Similar to the Selenium project, these test scripts are built with the Page Object Design pattern for efficient maintenance and execution.

Project Structure:

Cypress_Cucumber_TestProject: The directory for the Cypress Cucumber framework project.
  - Integration/BDD: This folder contains subdirectories, each dedicated to testing scripts for different web applications, all organized using fixtures and the Page Object Design pattern:
      - RegistrationForm: Functional test cases for a registration page on an e-commerce website.
      - Veg Delivery: Functional test scripts for another e-commerce website.
      - Ecommerce: Functional test cases of another shopping website.
      - API_BookLibrary: Test cases that include API calls, mocking API requests, and responses for an e-library.
      - PageObjects: All the page object classes can be found in this folder.
  - fixtures/example: This contains the test data that is fed to the test cases via fixtures.

Additional Information
For Cypress Cucumber test scripts, it is possible to connect with the Cypress Cloud to access and review logs for test executions. 
