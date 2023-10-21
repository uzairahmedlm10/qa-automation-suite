from selenium.webdriver.common.by import By


class checkoutPage:

    def __init__(self,driver):
        self.driver = driver

    promo = (By.CSS_SELECTOR, ".promoCode")
    applyBtn = (By.CLASS_NAME, "promoBtn")
    promo_msg = (By.CSS_SELECTOR, ".promoInfo")
    totalAmt = (By.CSS_SELECTOR,".totAmt")
    discount = (By.CLASS_NAME, "discountPerc")
    DiscountedTotal = (By.CSS_SELECTOR, ".discountAmt")
    placeOrder = (By.XPATH, "//button[text()='Place Order']")
    countryDropdown = (By.XPATH, "//select")
    TC_checkbox = (By.CLASS_NAME, "chkAgree")
    proceed = (By.XPATH, "//button[text()='Proceed']")
    ConfirmAlert = (By.CSS_SELECTOR, ".wrapperTwo")

    def promoBox(self):
        return self.driver.find_element(*checkoutPage.promo)

    def ApplyButton(self):
        return self.driver.find_element(*checkoutPage.applyBtn)

    def promoMessage(self):
        return self.driver.find_element(*checkoutPage.promo_msg)

    def total_amount(self):
        return self.driver.find_element(*checkoutPage.totalAmt)

    def discountText(self):
        return self.driver.find_element(*checkoutPage.discount)

    def TotalAfterDiscount(self):
        return self.driver.find_element(*checkoutPage.DiscountedTotal)

    def placeOrder_button(self):
        return self.driver.find_element(*checkoutPage.placeOrder)

    def country_dropdown(self):
        return self.driver.find_element(*checkoutPage.countryDropdown)

    def TermsnConditions(self):
        return self.driver.find_element(*checkoutPage.TC_checkbox)

    def proceedBtn(self):
        return self.driver.find_element(*checkoutPage.proceed)

    def confirm_message(self):
        return self.driver.find_element(*checkoutPage.ConfirmAlert)