from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SimpleSeleniumScript:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

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
    script = SimpleSeleniumScript()
    script.open_link(link=url)
    script.wait_until_element_present_by_xpath(xpath_wait_id='//*[@id="id_username"]')
    script.fill_form(info_to_fill={'//*[@id="id_username"]': 'Username', '//*[@id="id_password"]': 'Pass'})
    script.click_button_by_xpath(xpath_button_id='//*[@id="login-form"]/div[4]/input')
    input("Press Enter to close the browser...")
    # Close the browser
    script.close_browser()
