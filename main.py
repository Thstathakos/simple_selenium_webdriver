from selenium_script import SeleniumScript
import logging


# This is an example of the script's functions you can change them according to your needs.
# You can use xpath,id,name as a locator see the file selenium_script.py for more details


if __name__ == "__main__":
    url = 'www.example.com'
    logging.basicConfig(level=logging.INFO)  # Set logging level
    script = SeleniumScript()
    try:
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
