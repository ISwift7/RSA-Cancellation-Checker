import winsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver to connect to an existing Chrome session
def initialize_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:????")  # Replace with the correct port number for Chrome debugger session
    driver = webdriver.Chrome(options=chrome_options)
    return driver

driver = initialize_driver()

# Function to check if any modal exists and close it
def close_modal():
    try:
        # Replace 'YOUR_MODAL_XPATH' with the actual XPath of the modal
        modal_present = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, 'YOUR_MODAL_XPATH'))  # Replace 'YOUR_MODAL_XPATH' with the actual XPath for modal detection
        )
        if modal_present:
            # Replace 'YOUR_CLOSE_BUTTON_XPATH' with the XPath of the modal's close button
            close_button = driver.find_element(By.XPATH, 'YOUR_CLOSE_BUTTON_XPATH')  # Replace with actual XPath
            close_button.click()
            print("Modal closed.")
    except Exception as e:
        print(f"Modal not present or couldn't be closed: {e}")

def open_map():
    try:
        # Replace 'YOUR_LOCATION_BUTTON_ID' with the actual ID of the Location button
        location_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'YOUR_LOCATION_BUTTON_ID'))  # Replace with actual button ID
        )
        location_button.click()
        print("Location button clicked.")

        # Replace 'YOUR_MORE_LOCATIONS_BUTTON_XPATH' with the XPath of the "More Locations" button
        more_locations_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, 'YOUR_MORE_LOCATIONS_BUTTON_XPATH'))  # Replace with actual XPath
        )
        more_locations_button.click()
        print("More Locations button clicked, map opened.")

    except Exception as e:
        print(f"Error opening map: {e}")

def check_for_test_centre_availability():
    try:
        # Replace 'YOUR_TEST_CENTRE_PIN_XPATH' with the actual XPath of the test centre pin on the map
        test_centre_pin = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, 'YOUR_TEST_CENTRE_PIN_XPATH'))  # Replace with actual XPath for the test centre pin
        )
        driver.execute_script("arguments[0].click();", test_centre_pin)  # Force click using JavaScript
        print("Test centre pin clicked.")

        # Replace 'YOUR_AVAILABILITY_DATE_XPATH' with the actual XPath of the date showing availability
        available_date_xpath = 'YOUR_AVAILABILITY_DATE_XPATH'  # Replace with actual XPath

        # Wait for the availability text to load
        available_date_element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, available_date_xpath))
        )

        available_date = available_date_element.text
        if "No availability" not in available_date:
            print(f"Available date found: {available_date}. Proceeding to book.")
            return True  # Slot available
        else:
            print("No available dates for the test centre.")
            return False  # No slot available

    except Exception as e:
        print(f"Error checking test centre availability: {e}")
        return False

def close_map():
    try:
        # Short delay before closing the map
        time.sleep(1)

        # Replace 'YOUR_CLOSE_MAP_BUTTON_XPATH' with the XPath of the map's close button
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 'YOUR_CLOSE_MAP_BUTTON_XPATH'))  # Replace with actual XPath
        )
        close_button.click()
        print("Map closed.")

    except Exception as e:
        print(f"Error closing map: {e}")

def select_and_confirm_test_centre():
    try:
        # Replace 'YOUR_SELECT_CENTRE_BUTTON_XPATH' with the XPath of the "Select Centre" button
        select_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 'YOUR_SELECT_CENTRE_BUTTON_XPATH'))  # Replace with actual XPath
        )
        select_button.click()
        print("Select Centre button clicked.")

        # Replace 'YOUR_CONFIRM_BUTTON_XPATH' with the XPath of the "Confirm" button
        confirm_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, 'YOUR_CONFIRM_BUTTON_XPATH'))  # Replace with actual XPath
        )
        confirm_button.click()

        print("Test slot successfully booked!")
        winsound.Beep(1000, 1000)  # Beep for 1 second (1000 ms) at 1000 Hz frequency

    except Exception as e:
        print(f"An error occurred during confirmation: {e}")

# Main function to run the script
def main():
    # Close the modal if it appears
    close_modal()

    while True:
        open_map()

        # Check for test centre availability
        if check_for_test_centre_availability():
            # If a test centre has an available date, select the centre and confirm booking
            select_and_confirm_test_centre()
            break  # Stop the script once booked
        else:
            # If no slots are available, close the map and wait before checking again
            close_map()
            print("Retrying in 30 seconds...")
            time.sleep(30)  # Wait 30 seconds before checking again

if __name__ == "__main__":
    main()
