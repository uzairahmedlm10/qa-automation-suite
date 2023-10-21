Project 1: Hubspot Account Verification From Gmail

Description:
In this project, we focus on automated account verification from Gmail using Selenium Webdriver and the Pytest framework. The tests are organized using the Page Object Design pattern for better code organization and maintenance.

Project Structure:
hubspot_VerifyAccount: The core directory for the Selenium Webdriver and Pytest framework project.

  - TestCases: This folder contains the test case file for connecting with gmail server and getting OTP to verify account on hubspot.
  - PageObjects: The page object class that facilitate the framework are stored in this folder.
  - Utilities: This folder contains the utility base class for resuable methods and fixture reference. This class are being inherited in the actual test cases.
  - TestData: This contains the data that is fed to the test case via fixture.

TestCases:
- VerifyOTP.py: This test file automates the process of user registration on the 'Hubspots' website. It integrates with a Gmail server to extract a One-Time Password (OTP) and activate the account on Hubspot. Like other scripts, it uses fixtures and inherits from a base class to ensure efficient test execution.
