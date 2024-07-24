from behave import *
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from scripts import browser_config, logger_config, tools


@given('I am using "{browser}"')
def setup_browser(context, browser):
    context.driver = browser_config.get_driver(browser)


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
    tools.capture_screenshot(context, "cart_with_two_products")


@when('I place the order with the following data')
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
    tools.capture_screenshot(context, "completed_form")

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
    tools.capture_screenshot(context, "successful_purchase")

@then('I should see the successful user registration dialog')
def step_then(context):
    WebDriverWait(context.driver, 10).until(ec.alert_is_present())

    # Click the accept button
    alert = context.driver.switch_to.alert
    assert alert.text == "Sign up successful."
    alert.accept()
    context.logger.info('Asserted that the successful sign up alert appears on screen.')

@when('I click on the "Sign up" button in the sign-up form')
def step_when(context):
    signup_text = WebDriverWait(context.driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "#signInModal .btn-primary"))
    )
    signup_text.click()
    context.logger.info('Clicked on the "Sign up" button in the sign-up form')

@when('I fill out the sign-up form with a non-existant, valid username and password')
def step_when(context):
    username_field = WebDriverWait(context.driver, 10).until(
        ec.element_to_be_clickable((By.ID, "sign-username"))
    )
    new_username = tools.append_random_hash(context.test_user)
    username_field.clear()
    username_field.send_keys(new_username)
    context.logger.info('Added valid username')
    
    password_field = WebDriverWait(context.driver, 10).until(
        ec.element_to_be_clickable((By.ID, "sign-password"))
    )

    password_field.send_keys(new_username)
    context.logger.info('Added valid password')
    tools.capture_screenshot(context, "filled_signup_form")
    
@when('I click on "Sign up" in the header')
def step_when(context):
    signup_button = WebDriverWait(context.driver, 10).until(
        ec.visibility_of_element_located((By.ID, "signin2"))
    )
    signup_button.click()
    context.logger.info('Clicked on "Sign up" in the header')

