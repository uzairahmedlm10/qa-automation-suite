Feature: E-commerce user registration form

    Fill out the registration form from a database for an ecommerce website

    # Scenario: Test two-way data binding textbox
    # Given I open the ecommerce home page
    # When I type Name from database in the textbox
    # Then I verify if the other textbox with data binding is also filled

    # Scenario: Verify if the 'entrepreneur' radio button is disabled regardless of the employment status
    # Given I open the ecommerce home page
    # When I select the employment status as 'student' and verify if the 'entrepreneur' button is disabled
    # Then I select the employment status as 'Employed' and verify if the 'entrepreneur' button is disabled

    # Scenario: Fill in the date of birth and verify the value
    # Given I open the ecommerce home page
    # When I type in the date from database
    # Then I put assertion to verify if the correct date has been filled in

    # Scenario: Submit the form and verify the success alert message
    # Given I open the ecommerce home page
    # When I fill in the form from database
    # Then I click submit and put assertion to verify if the correct alert message appears