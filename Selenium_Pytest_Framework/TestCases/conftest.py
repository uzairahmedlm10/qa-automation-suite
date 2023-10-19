import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browserName", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser = request.config.getoption("--browserName")
    if browser == "chrome":
        services = Service("C:/Users/User/Downloads/Selenium/chromedriver.exe")
        driver = webdriver.Chrome(service=services)
    elif browser == "firefox":
        services = Service("C:/Users/User/Downloads/Selenium/geckodriver.exe")
        driver = webdriver.Firefox(service=services)

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope='class')
def setup_hubspot(request):
    global driver
    browser = request.config.getoption("--browserName")
    if browser == "chrome":
        services = Service("C:/Users/User/Downloads/Selenium/chromedriver.exe")
        driver = webdriver.Chrome(service=services)
    elif browser == "firefox":
        services = Service("C:/Users/User/Downloads/Selenium/geckodriver.exe")
        driver = webdriver.Firefox(service=services)

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://app.hubspot.com/signup-hubspot/crm?hubs_signup-cta=login-signup-cta&hubs_signup-url=app.hubspot.com%2Flogin&uuid=5b9b2b8b-16e3-4d65-889f-a6fb94012594&step=landing_page")

    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

