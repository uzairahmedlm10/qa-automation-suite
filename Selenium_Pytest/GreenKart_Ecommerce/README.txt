Project: Functional Testing of an E-commerce Website for Vegetables

Description:
In this project, we focus on automated testing of an e-commerce website using Selenium Webdriver and the Pytest framework. The tests are organized using the Page Object Design pattern for better code organization and maintenance.

Project Structure:
Selenium_Pytest_Framework: The core directory for the Selenium Webdriver and Pytest framework project.

  - TestCases: This folder contains functional test scripts for an e-commerce website.
  - PageObjects: All page object classes that facilitate the framework are stored in this folder.
  - Utility: This folder contains the utility base classes for the respective websites. These classes are being inherited in the actual test cases.
  - TestData: This contains the data that is fed to the test cases via fixtures.

TestCases:
- SearchProducts.py: This file contains functional test cases related to the e-commerce website. Test scenarios are documented within comments, and the script makes use of fixtures and a base class to streamline test execution.
