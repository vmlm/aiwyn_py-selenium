from behave import *
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from scripts import browser_manager, logger_manager


@given('I am using {browser}')
def setup_browser(context, browser):
    # Set the WDM logger level to ERROR, so we don't get webdriver configuration messages
    logger_manager.set_logger_level_error('WDM')
    context.driver = browser_manager.get_driver(browser)


@when('I navigate to the demoblaze home page')
def navigate_home(context):
    context.driver.get(context.home_url)

    # Wait for the page to load before logging
    WebDriverWait(context.driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "h4.card-title > a.hrefch"))
    )
    context.logger.info("Navigated to Demoblaze home page.")


@when('I add two random products to the cart')
def add_2_random_products(context):
    for i in range(2):
        # Only consider products on the first page for testing purposes
        products_on_first_page = context.driver.find_elements(By.CSS_SELECTOR, "h4.card-title > a.hrefch")

        # Select a product at random and add it to the cart.
        selected_product = products_on_first_page[random.randint(0, len(products_on_first_page) - 1)]
        add_product(context, selected_product)

        # Reset so we always start at Home for the next action.
        navigate_home(context)


def add_product(context, product):
    # Click product link and navigate to the product page
    product_text = product.text
    product.click()

    add_product_button = WebDriverWait(context.driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "div.col-sm-12.col-md-6.col-lg-6 > a.btn.btn-success.btn-lg"))
    )
    context.logger.info(f"Navigated to product page for {product_text}")

    # Click the add to cart button and wait for alert to pop up
    # onclick = add_product_button.get_attribute('onclick')
    # context.driver.execute_script(f"{onclick};")
    add_product_button.click()
    context.logger.info("Clicked the 'Add to Cart' button using JavaScript")
    WebDriverWait(context.driver, 10).until(ec.alert_is_present())

    # Click the accept button
    alert = context.driver.switch_to.alert
    alert.accept()
    context.logger.info(f"Added {product_text} to the cart")


@when('I visualize the cart')
def navigate_to_cart(context):
    # Wait for the Cart link to be available
    cart_link = WebDriverWait(context.driver, 10).until(
        ec.element_to_be_clickable((By.LINK_TEXT, "Cart"))
    )
    cart_link.click()

    WebDriverWait(context.driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, "tbody > tr.success"))
    )

    context.logger.info("Navigated to cart page")
    capture_screenshot(context, "cart_with_two_products")


@when('I the place order with the following data')
def place_order(context):
    place_order_button = context.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success")

    # Click the place order button and wait for the form to load
    place_order_button.click()
    WebDriverWait(context.driver, 10).until(
        ec.presence_of_all_elements_located((By.TAG_NAME, 'input'))
    )

    # Fill out the form
    for row in context.table:
        input_field = WebDriverWait(context.driver, 10).until(
            ec.element_to_be_clickable((By.ID, row[0].lower()))
        )
        input_field.clear()
        input_field.send_keys(row[1])

    context.logger.info("Completed the form...")
    capture_screenshot(context, "completed_form")

    purchase_button = WebDriverWait(context.driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//button[text()='Purchase']"))
    )

    purchase_button.click()
    context.logger.info("Placed an order...")


@then('I should see the successful purchase screen')
def check_successful_purchase(context):
    # Wait for the success screen to load
    WebDriverWait(context.driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "div.sa-icon.sa-success.animate"))
    )
    context.logger.info("And verified the successful purchase screen")
    capture_screenshot(context, "successful_purchase")


def capture_screenshot(context, step_name):
    screenshot_path = f"{context.screenshots_dir}/{step_name}.png"
    context.driver.save_screenshot(screenshot_path)


# if __name__ == "__main__":
#     class ContextDummy(object):
#         driver = None
#         home_url = ""
#         table = [{
#             'Name': 'John Doe',
#             'Country': 'USA',
#             'City': 'New York',
#             'Card': '1234 5678',
#             'Month': '12',
#             'Year': '2024'
#         }, ]
#         screenshots_dir = ''
#
#
#     dummy_context = ContextDummy()
#     setup_browser(dummy_context, "Chrome")
#     navigate_home(dummy_context, "https://www.demoblaze.com")
#     add_2_random_products(dummy_context)
#     navigate_to_cart(dummy_context)
#     place_order(dummy_context)
