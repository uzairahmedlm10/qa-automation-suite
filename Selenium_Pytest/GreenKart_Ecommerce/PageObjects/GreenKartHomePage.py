from selenium.webdriver.common.by import By

from PageObjects.GreenKartCheckout import checkoutPage
from PageObjects.GreenKartTopDeals import TopDealsPage


class homepageGK:

    def __init__(self, driver):
        self.driver = driver

    search_box = (By.CLASS_NAME, "search-keyword")
    items = (By.CSS_SELECTOR, "h4")
    cartItems = (By.CSS_SELECTOR, "tr td:nth-child(3) strong")
    add_to_cart = (By.CSS_SELECTOR, "button[type='button']")
    increment = (By.CSS_SELECTOR, ".increment")
    productPrice = (By.CSS_SELECTOR, "p")
    product = (By.CSS_SELECTOR, ".product")
    topdeals = (By.LINK_TEXT, "Top Deals")
    checkout = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    cartImg = (By.CSS_SELECTOR, "[alt='Cart']")

    def searchBox(self):
        return self.driver.find_element(*homepageGK.search_box)

    def getItems(self, X):
        return X.find_element(*homepageGK.items)

    def cartCount(self):
        return self.driver.find_elements(*homepageGK.cartItems)

    def cartbutton(self,T):
        return T.find_element(*homepageGK.add_to_cart)

    def incrementbtn(self, Y):
        return Y.find_element(*homepageGK.increment)

    def ProductPrice(self, Z):
        return Z.find_element(*homepageGK.productPrice)

    def products(self):
        return self.driver.find_elements(*homepageGK.product)

    def dealsbtn(self):
        self.driver.find_element(*homepageGK.topdeals).click()
        return TopDealsPage(self.driver)
    def checkout_button(self):
        self.driver.find_element(*homepageGK.checkout).click()
        return checkoutPage(self.driver)

    def cartImage(self):
        return self.driver.find_element(*homepageGK.cartImg)