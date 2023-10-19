Feature: E-commerce website testing

    Functional test cases of an ecommerce website


    # Scenario: verify the blinking message text on the dashboard page
    # Given I make the api call to the ecommerce site and bypass the login page by passing the session token
    # When I get the text of the blinking message
    # Then I verify the text

    # Scenario: Verify the toast message after adding a product to the cart and ensure that it goes away immediately
    # Given I make the api call to the ecommerce site and bypass the login page by passing the session token
    # When I add a product to the cart, I extract the toast message
    # Then I verify the text in the toast message and put assertion that notification goes away immediately
    
    # Scenario: Filter products from homepage based on search results
    # Given I make the api call to the ecommerce site and bypass the login page by passing the session token
    # When I type characters in the searchbox to search a product from dashboard
    # Then I put assertion on the products to verify if they have been correctly filtered based on the search result

    # Scenario: Fill out billing and shipping information
    # Given I make the api call to the ecommerce site and bypass the login page by passing the session token
    # When I iterate through all the products to find a specific product and add it to the cart
    # Then I go to the cart page and fill out the billing and shipping information with some assertions and apply coupon

    # Scenario: Download order details in a csv file and verify data
    # Given I make the api call to the ecommerce site and bypass the login page by passing the session token
    # When I iterate through all the products to find a specific product and add it to the cart
    # Then I go to the cart page and fill out the billing and shipping information with some assertions and apply coupon
    # And I download the order details in a csv file and verify data inside with assertions

    # Scenario: Verify the number of orders after deleting an order
    # Given I make the api call to the ecommerce site and bypass the login page by passing the session token
    # When I go to the orders page and count the total number of orders
    # Then I delete an order and verify the number again
