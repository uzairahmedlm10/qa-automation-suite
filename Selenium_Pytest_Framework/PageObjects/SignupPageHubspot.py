from selenium.webdriver.common.by import By


class signup:

    def __init__(self, driver):
        self.driver = driver

    email = (By.CSS_SELECTOR, "[type='email']")
    verifybtn = (By.XPATH, "//i18n-string[text()='Verify email']")
    Otpinput = (By.CSS_SELECTOR, "[type='text']")
    nextbtn = (By.XPATH, "//i18n-string[text()='Next']")

    def emailbox(self):
        return self.driver.find_element(*signup.email)

    def verify(self):
        return self.driver.find_element(*signup.verifybtn)

    def OTP_Input(self):
        return self.driver.find_elements(*signup.Otpinput)

    def Next_button(self):
        return self.driver.find_element(*signup.nextbtn)


