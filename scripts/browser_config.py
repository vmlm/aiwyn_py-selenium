from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import platform

supported_browsers = ["Chrome", "Firefox", "Edge"]


def get_driver(browser):
    # Initialize the WebDriver and add it to the context
    if browser not in supported_browsers:
        raise ValueError(f"Unsupported browser: {browser}")

    driver = None
    browser_options = __get_browser_conf(browser)
    if browser == 'Chrome':
        from selenium.webdriver.chrome.service import Service as ChromeService
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=browser_options
        )
    elif browser == 'Firefox':
        # Setup for Firefox (similar approach)
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=browser_options
        )
    elif browser == 'Edge':
        # Setup for Edge (similar approach)
        from selenium.webdriver.edge.service import Service as EdgeService
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=browser_options
        )

    try:
        WebDriverWait(driver, 60).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
    except Exception as e:
        raise RuntimeError("WebDriver initialization timed out or failed to load the browser") from e

    return driver


def __get_browser_conf(browser):
    options = None
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
    elif browser == "Firefox":
        options = webdriver.FirefoxOptions()
    elif browser == "Edge":
        options = webdriver.EdgeOptions()

    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--window-size=1920x1080")  # Set the window size for the screenshot
    options.add_argument("--log-level=3")  # Suppress all console log

    if platform.system() == "Windows":
        options.add_argument("--disable-gpu")  # GPU in Windows may cause errors

    return options
