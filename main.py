from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging


class SeleniumScript:
    def __init__(self, browser_type="chrome"):
        try:
            if browser_type.lower() == "chrome":
                self.driver = webdriver.Chrome()
            # Add other browser options as needed
            else:
                raise ValueError("Invalid browser type specified.")
            self.wait = WebDriverWait(self.driver, 10)
        except Exception as e:
            logging.error(f"Error initializing WebDriver: {str(e)}")
            raise

    def wait_for_element(self, locator_method, value):
        try:
            by = self._get_by_method(locator_method)
            self.wait.until(EC.presence_of_element_located((by, value)))
        except Exception as e:
            logging.warning(f"Element not found: {str(e)}")

    def open_link(self, link):
        # Open the link
        self.driver.get(link)

    def fill_form(self, info_to_fill):
        for locator_method, value in info_to_fill.items():
            method, xpath = locator_method.split(':', 1)  # Split the locator method and XPath
            by = self._get_by_method(method)
            input_field = self.driver.find_element(by, xpath)
            input_field.send_keys(value)

    def click_button(self, locator_method, value):
        by = self._get_by_method(locator_method)
        button_element = self.driver.find_element(by, value)
        button_element.click()

    def wait_until_element_present(self, locator_method, value):
        by = self._get_by_method(locator_method)
        self.wait.until(EC.presence_of_element_located((by, value)))

    def _get_by_method(self, locator_method):
        locator_method = locator_method.lower()
        if locator_method == "xpath":
            return By.XPATH
        elif locator_method == "id":
            return By.ID
        elif locator_method == "name":
            return By.NAME
        else:
            raise ValueError("Invalid locator method specified.")

    def close_browser(self):
        # Close the browser window
        self.driver.quit()


if __name__ == "__main__":
    url = 'https://www.example.com'
    logging.basicConfig(level=logging.INFO)  # Set logging level
    try:
        script = SeleniumScript()
        script.open_link(url)
        script.wait_for_element("xpath", '//*[@id="id_username"]')
        script.fill_form({'id:id_username': 'Username', 'name:password': 'Pass'})
        script.click_button("xpath", '//*[@id="login-form"]/div[4]/input')
        input("Press Enter to close the browser...")
        script.close_browser()
    except Exception as exception:
        logging.error(f"Test execution failed: {str(exception)}")
    finally:
        script.close_browser()
