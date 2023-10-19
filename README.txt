This repository contains two projects for quality assurance (QA) automation testing. Both projects are built using modern testing frameworks and follow the Page Object Design (POD) pattern for enhanced maintainability.

Project 1: Selenium Webdriver with Pytest (Python)

Project Structure:

Selenium_Pytest_Framework: The core directory for the Selenium Webdriver and Pytest framework project.
TestCases: This folder contains functional test scripts for an e-commerce website.
SearchProducts.py: Functional test cases are detailed in comments, covering various scenarios. This script utilizes fixtures and inherits a base class for enhanced code reusability.
PageObjects: All page object classes that facilitate the framework are stored in this folder.
Description
In this project, we focus on automated testing of an e-commerce website using Selenium Webdriver and the Pytest framework. The tests are organized using the Page Object Design pattern for better code organization and maintenance.

Test Cases
SearchProducts.py: This file contains functional test cases related to the e-commerce website. Test scenarios are documented within comments, and the script makes use of fixtures and a base class for streamlined test execution.

VerifyOTP.py: This test file automates the process of user registration on the 'Hubspots' website. It integrates with a Gmail server to extract a One-Time Password (OTP) and activate the account on Hubspot. Like other scripts, it uses fixtures and inherits from a base class to ensure efficient test execution.

Project 2: Cypress Cucumber Framework (JavaScript)
Project Structure
Cypress_Cucumber_TestProject: The directory for the Cypress Cucumber framework project.
Integration/BDD: This folder contains subdirectories, each dedicated to testing scripts for different web applications.
RegistrationForm: Functional test cases for a registration page on an e-commerce website.
Veg Delivery: Functional test scripts for another e-commerce website.
Ecommerce: Additional functional test cases for a different shopping website.
API_BookLibrary: Test cases that include API calls, mocking API requests, and responses for an e-library.
Description
In this project, we utilize the Cypress Cucumber framework to automate testing for various web applications. Similar to the Selenium project, these test scripts are built with the Page Object Design pattern for efficient maintenance and execution.

Test Cases
The project includes test scripts for the following web applications, all organized using fixtures and the Page Object Design pattern:

RegistrationForm: Test scenarios for the registration page of an e-commerce website.
Veg Delivery: Functional test cases for an e-commerce website.
Ecommerce: Additional functional test cases for a different shopping website.
API_BookLibrary: Test cases that involve API calls, mocking API requests, and responses for an e-library.
Additional Information
All test cases in both projects follow the Page Object Design pattern for maintainability and efficiency.
The respective Page Object classes are stored in the 'PageObjects' folders within their respective project directories.
For Cypress Cucumber test scripts, it is possible to connect with the Cypress Cloud to access and review logs for test executions.