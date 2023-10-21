from selenium.webdriver.common.by import By


class TopDealsPage:

    def __init__(self, driver):
        self.driver = driver

    dropdown = (By.ID, "page-menu")
    tableitems = (By.CSS_SELECTOR, "tbody tr td:nth-child(1)")
    sortbtn = (By.XPATH,"//span[text()='Veg/fruit name']")
    searchbox = (By.ID, "search-field")
    price = (By.CSS_SELECTOR, "tbody tr td:nth-child(2)")
    discount = (By.CSS_SELECTOR, "tbody tr td:nth-child(3)")
    lastPage = (By.CSS_SELECTOR, "[aria-label='Last']")
    highlighted = (By.CSS_SELECTOR, "li[class='active'] a span:nth-child(1)")
    firstPage = (By.CSS_SELECTOR, "[aria-label='First']")
    secondPage = (By.XPATH, "//span[text()='2']")
    deliveryData = (By.CSS_SELECTOR, "[type='date']")


    def dropdownBtn(self):
        return self.driver.find_element(*TopDealsPage.dropdown)

    def table_items(self):
        return self.driver.find_elements(*TopDealsPage.tableitems)

    def sort_button(self):
        return self.driver.find_element(*TopDealsPage.sortbtn)

    def search(self):
        return self.driver.find_element(*TopDealsPage.searchbox)

    def item_price(self):
        return self.driver.find_elements(*TopDealsPage.price)

    def item_discount(self):
        return self.driver.find_elements(*TopDealsPage.discount)

    def last_page(self):
        return self.driver.find_element(*TopDealsPage.lastPage)

    def highlightPage(self):
        return self.driver.find_element(*TopDealsPage.highlighted)

    def first_page(self):
        return self.driver.find_element(*TopDealsPage.firstPage)

    def second_page(self):
        return self.driver.find_element(*TopDealsPage.secondPage)

    def delievery_date(self):
        return self.driver.find_element(*TopDealsPage.deliveryData)

