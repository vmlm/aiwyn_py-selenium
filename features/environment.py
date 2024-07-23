import os
from datetime import datetime
from scripts import logger_manager



def before_all(context):
    # Setup directories for results and screenshots
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    context.results_dir = f"./results/{timestamp}"
    context.screenshots_dir = f"{context.results_dir}/screenshots"
    os.makedirs(context.screenshots_dir, exist_ok=True)
    context.logger = logger_manager.configure_logger(context)

    # Setup home and api urls
    context.home_url = 'https://www.demoblaze.com/'
    context.api_url = 'https://api.demoblaze.com'

    # Setup api endpoints
    context.signup_endpoint = '/signup'
    context.login_endpoint = '/login'

    # base name for test users
    context.test_user = 'mucker'


def after_scenario(context, scenario):
    # Quit the WebDriver after each scenario
    if hasattr(context, 'driver'):
        context.driver.quit()
