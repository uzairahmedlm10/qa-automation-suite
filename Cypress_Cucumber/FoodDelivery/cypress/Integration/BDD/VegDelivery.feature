Feature: Food Delivery

    Order vegetables from an ecommerce store


    Scenario: Search vegetables starting from 'ca' and add to cart
    Given I go to the ecommerce website
    When I filter vegetables from the search box
    And Add to cart
    Then I go to the cart page


    Scenario: Verify total price in the cart
    Given I go to the ecommerce website
    When I filter vegetables from the search box
    And Add to cart
    Then I verify the total price in the cart


    Scenario: Check if the promo code works
    Given I go to the ecommerce website
    When I filter vegetables from the search box
    And Add to cart
    Then I go to the cart page
    And Apply promo code,wait and verify the discounted price

    Scenario: Place Order without agreeing to terms and conditions
    Given I go to the ecommerce website
    When I filter vegetables from the search box
    And Add to cart
    Then I go to the cart page
    And select country and place order without agreeing to terms

    Scenario: Check terms & condition checkbox and place order
    Given I go to the ecommerce website
    When I filter vegetables from the search box
    And Add to cart
    Then I go to the cart page
    And agree to terms and condition, place order and verify the 'success' message

    Scenario: Handling of the separate tab
    Given I go to the ecommerce website
    When I filter vegetables from the search box
    And Add to cart
    Then I go to the cart page
    And I go to the terms and conditions tab and then i go to the home page
    And I verify the url with an assertion

    Scenario: Check if the sum of the individual items in the cart table matches with the total price mentioned
    Given I go to the ecommerce website
    When I filter vegetables from the search box
    And Add to cart
    Then I go to the cart page
    And verify if the items in the cart table makes the equal sum of the total amount mentioned