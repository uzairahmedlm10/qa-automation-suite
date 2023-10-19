import time

from selenium import webdriver

from PageObjects.GreenKartHomePage import homepageGK
from Utilities.utilityGreenKart import BaseClass


class TestGreenKart(BaseClass):
    driver: webdriver  # type hinting

# search products with characters and verify if the filtered items actually start with these characters
    def test_searchProducts(self):
        homepage = homepageGK(self.driver)
        homepage.searchBox().send_keys("ca")
        time.sleep(2)
        products = homepage.products()
        for product in products:
            if product.is_displayed():
                product_name = homepage.getItems(product).text
                assert product_name.startswith("Ca")

 # verify the number of items in the cart after adding some products to it
    def test_verifyCartCount(self):
        homepage = homepageGK(self.driver)
        homepage.searchBox().send_keys("ca")
        time.sleep(2)
        products = homepage.products()
        for product in products:
            if product.is_displayed():
                homepage.cartbutton(product).click()

        cart = homepage.cartCount()
        cart_item_count = int(cart[0].text)
        assert cart_item_count == 4

 # increment the item quantity and verify the amount on the cart image
    def test_incrementButton(self):
        homepage = homepageGK(self.driver)
        AllProducts = homepage.products()
        for product in AllProducts:
            productTitle = homepage.getItems(product).text
            if 'Cashews' in productTitle:
                price = int(homepage.ProductPrice(product).text)
                i = 1
                while i < 4:

                    homepage.incrementbtn(product).click()
                    i += 1
                homepage.cartbutton(product).click()
                break

        cart = homepage.cartCount()
        cart_item_count = int(cart[1].text)

        assert cart_item_count == price * i

 # change page size and verify the number of contents on the page
    def test_pageSize(self):
        homepage = homepageGK(self.driver)
        dealsPage = homepage.dealsbtn()

        self.window_tabs(1)  # defined in base class

        page_size = '20'
        self.dropdown(dealsPage.dropdownBtn(), page_size)  # calling from base class

        tableItems = dealsPage.table_items()
        table_size = len(tableItems)

        assert table_size <= int(page_size)

  # sort the veg table and verify if the items are correctly sorted
    def test_sorting(self):

        homepage = homepageGK(self.driver)
        dealsPage = homepage.dealsbtn()

        self.window_tabs(1)
        # dealsPage.sort_button().click()
        Items = dealsPage.table_items()

        ActualList = []

        for item in Items:
            item_name = item.text
            ActualList.append(item_name)

        SortedList = ActualList.copy()
        SortedList.sort()

        assert SortedList == ActualList

 # search the items table and verify if the searched letters exist in the table items
    def test_searchItems(self):
        homepage = homepageGK(self.driver)
        dealsPage = homepage.dealsbtn()
        self.window_tabs(1)

        search = 'rr'
        dealsPage.search().send_keys(search)
        Items = dealsPage.table_items()

        for item in Items:
            title = item.text
            assert search in title

#  Verify that discounted price is always less than the original price
    def test_verifyDiscountedPrice(self):
        homepage = homepageGK(self.driver)
        dealsPage = homepage.dealsbtn()
        self.window_tabs(1)

        Prices = dealsPage.item_price()
        Discounted = dealsPage.item_discount()

        i = 0
        while i < len(Prices):
            DisPrice = int(Discounted[i].text)
            OrigPrice = int(Prices[i].text)
            assert  DisPrice < OrigPrice
            i += 1

# verify if the last page gets active on clicking the last page button
    def test_lastPageActive(self):
        homepage = homepageGK(self.driver)
        dealsPage = homepage.dealsbtn()
        self.window_tabs(1)

        dealsPage.last_page().click()
        activePage = int(dealsPage.highlightPage().text)

        assert activePage == 4

# verify if the buttons get activated and disabled correctly on navigation
    def test_firstPageActive(self):
        homepage = homepageGK(self.driver)
        dealsPage = homepage.dealsbtn()
        self.window_tabs(1)


        dealsPage.second_page().click()

        dealsPage.first_page().click()
        activePage = int(dealsPage.highlightPage().text)

        assert activePage == 1

        assert dealsPage.first_page().get_attribute("aria-disabled") == 'true'

# Verify if the delivery date is today's date
    def test_deliveryDate(self):
        homepage = homepageGK(self.driver)
        dealsPage = homepage.dealsbtn()
        self.window_tabs(1)

        deliveryDate = dealsPage.delievery_date().get_attribute('value')
        today = date.today()

        d1 = today.strftime("%Y-%m-%d")

        assert deliveryDate == d1

# Apply promo code and verify the total amount after discount and put some assertions on discount and total
    def test_verifyPromo(self):
        homepage = homepageGK(self.driver)

        homepage.searchBox().send_keys("ca")
        time.sleep(2)
        products = homepage.products()
        for product in products:
            if product.is_displayed():
                homepage.cartbutton(product).click()

        homepage.cartImage().click()
        checkout = homepage.checkout_button()

        checkout.promoBox().send_keys("rahulshettyacademy")
        checkout.ApplyButton().click()

        self.waitOnVisibility(checkout.promo_msg) # defined in the base class

        assert checkout.promoMessage().text == "Code applied ..!"

        Total = int(checkout.total_amount().text)
        discountPerc = checkout.discountText().text
        Discounted = float(checkout.TotalAfterDiscount().text)

        assert discountPerc != '0%'

        discountNum = int(discountPerc.strip("%"))

        percentage = discountNum/100

        ExpectedTotal = Total - (Total * percentage)

        assert ExpectedTotal == Discounted

# Place an order and deliver it to any country and put assertions on the confirmation message and the url
    def test_orderDelivery(self):

        homepage = homepageGK(self.driver)
        homepage.searchBox().send_keys("ca")
        time.sleep(2)
        products = homepage.products()
        for product in products:
            if product.is_displayed():
                homepage.cartbutton(product).click()

        homepage.cartImage().click()
        checkout = homepage.checkout_button()

        checkout.placeOrder_button().click()
        country = "India"
        self.dropdown(checkout.country_dropdown(), country)
        checkout.TermsnConditions().click()
        checkout.proceedBtn().click()
        Confirmation = checkout.confirm_message()
        Confirm_Text = Confirmation.text

        assert "Thank you" in Confirm_Text
        time.sleep(5)
        assert self.driver.current_url == "https://rahulshettyacademy.com/seleniumPractise/#/"











