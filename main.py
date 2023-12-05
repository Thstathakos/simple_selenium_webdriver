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

    def wait_for_element(self, by, value):
        try:
            self.wait.until(EC.presence_of_element_located((by, value)))
        except Exception as e:
            logging.warning(f"Element not found: {str(e)}")

    def open_link(self, link):
        # Open the link
        self.driver.get(link)

    def fill_form(self, info_to_fill):
        # Find the input boxes by their IDs and fill in the information
        for xpath_id, value in info_to_fill.items():
            input_field = self.driver.find_element(By.XPATH, xpath_id)
            input_field.send_keys(value)

    def click_button_by_xpath(self, xpath_button_id):
        # Example: Click the "Confirm" button with a specific ID
        confirm_button = self.driver.find_element(By.XPATH, xpath_button_id)
        confirm_button.click()

    def wait_until_element_present_by_xpath(self, xpath_wait_id):
        # Wait until an element with the specified CSS selector is present
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath_wait_id)))

    def close_browser(self):
        # Close the browser window
        self.driver.quit()


if __name__ == "__main__":
    url = 'https://example_url.com'
    logging.basicConfig(level=logging.INFO)  # Set logging level
    try:
        script = SeleniumScript()
        script.open_link(url)
        script.wait_for_element(By.XPATH, '//*[@id="id_username"]')
        script.fill_form({'//*[@id="id_username"]': 'Username', '//*[@id="id_password"]': 'Pass'})
        script.click_button_by_xpath('//*[@id="login-form"]/div[4]/input')
        input("Press Enter to close the browser...")
    except Exception as exception:
        logging.error(f"Test execution failed: {str(exception)}")
    finally:
        script.close_browser()
