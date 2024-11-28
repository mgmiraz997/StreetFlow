from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time


# Function to convert AM/PM time to 24-hour time format
def convert_to_24hr_format(time_str):
    try:
        time_obj = datetime.strptime(time_str, "%I:%M %p")
        return time_obj.strftime("%H:%M")
    except ValueError as e:
        print(f"Error converting time: {e}")
        return None


# Setup Selenium WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the web page
driver.get("http://127.0.0.1:8000/form-search-bus/")

# Updated Search Form Test Function
def test_search_form_submit():
    try:
        # Wait for the form to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'name'))
        )

        # Fill out the form
        driver.find_element(By.NAME, 'name').send_keys("ena1")
        driver.find_element(By.NAME, 'source').send_keys("dhaka")
        driver.find_element(By.NAME, 'destination').send_keys("amtoli")

        # Convert time from AM/PM to 24-hour format
        time_am_pm = "02:30 PM"
        time_24hr = convert_to_24hr_format(time_am_pm)
        if not time_24hr:
            raise ValueError("Invalid time format provided.")

        # Fill the time input with the converted 24-hour time
        time_input = driver.find_element(By.NAME, 'time')
        time_input.send_keys(time_24hr)

        # Wait for the Search button to be clickable
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Search')]"))
        )

        # Scroll the button into view and try to click
        driver.execute_script("arguments[0].scrollIntoView(true);", search_button)
        try:
            search_button.click()
        except ElementClickInterceptedException:
            print("Click intercepted. Checking for overlays...")
            # Handle overlay if it exists
            try:
                overlay = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "overlay"))  # Replace with your overlay selector
                )
                if overlay.is_displayed():
                    print("Overlay found. Closing overlay...")
                    close_button = driver.find_element(By.CLASS_NAME, "close-button")  # Replace with your close button
                    close_button.click()
                    time.sleep(5)  # Allow overlay to close
                    search_button.click()  # Retry clicking the button
            except TimeoutException:
                print("No overlay found. Retrying click...")
                search_button.click()

        # Wait for results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'card'))
        )

        # Verify results are displayed
        buses_list = driver.find_elements(By.CLASS_NAME, 'card')
        assert len(buses_list) > 0, "No buses found."

        print("Test Passed: Search form successfully submitted, and buses are displayed.")

    except TimeoutException as e:
        print(f"Test Failed: Timeout occurred - {e}")
    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except AssertionError as e:
        print(f"Test Failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()

