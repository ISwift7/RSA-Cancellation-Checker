

---

# Test Centre Availability Checker and Auto-Booking Script

This script automates the process of checking availability at a specific test centre and confirming a slot if one becomes available. It uses **Selenium** for web automation, allowing the script to interact with the website's elements like buttons, modals, and availability listings.

## Features:
- Automatically checks for available test slots at a specified test centre.
- Closes pop-up modals (if present) to allow the rest of the process to continue.
- Opens the location map and checks the availability of test slots.
- If a slot is available, it selects and confirms the booking but you must do the payment and steps after yourself.
- A sound notification alerts you when a booking is successfully confirmed.

## Requirements

Before you can use this script, make sure you have the following set up:

### 1. Software and Packages:
- **Python 3.x** installed on your machine. [Download Python](https://www.python.org/downloads/)
- **Google Chrome** installed.
- **ChromeDriver** compatible with your version of Chrome. [Download ChromeDriver](https://sites.google.com/chromium.org/driver/)
- **Selenium WebDriver** for Python. Install it using:
  ```bash
  pip install selenium
  ```
- **Winsound** is included with Python, no additional installation is needed for Windows users.

### 2. Enable Remote Debugging in Chrome:
To allow the script to connect to an existing Chrome session, you must start Chrome with debugging enabled. You can do this by running Chrome from the command line with the following command:
```bash
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\path\to\your\chrome\profile"
```
Replace `C:\path\to\your\chrome\profile` with the actual path to your Chrome user data directory.

### 3. Configure the Script:
You’ll need to replace some placeholders in the script with the actual IDs, XPaths, and button text that match the website you are interacting with.

## Usage Instructions

Follow these steps to use the script:

### Step 1: Set Up the Debugging Session
1. Open a command prompt or terminal window.
2. Start Chrome in debugging mode by running the command:
   ```bash
   chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\path\to\your\chrome\profile"
   ```
   This opens a Chrome instance that the script will connect to.

### Step 2: Update Placeholders in the Script
1. Open the script file in your preferred text editor.
2. Find and replace the following placeholders with the appropriate values from the website you are automating:
    - `YOUR_MODAL_XPATH`: XPath for any modal pop-ups that need to be closed.
    - `YOUR_LOCATION_BUTTON_ID`: The ID of the button that opens the location map.
    - `YOUR_MORE_LOCATIONS_BUTTON_XPATH`: XPath for the "More Locations" button.
    - `YOUR_TEST_CENTRE_PIN_XPATH`: XPath for the test centre pin on the map.
    - `YOUR_AVAILABILITY_DATE_XPATH`: XPath for the date or availability text.
    - `YOUR_SELECT_CENTRE_BUTTON_XPATH`: XPath for the "Select Centre" button.
    - `YOUR_CONFIRM_BUTTON_XPATH`: XPath for the "Confirm" button to finalize the booking.

### Step 3: Run the Script
1. Once you've replaced the placeholders, save the script.
2. Run the script using Python:
   ```bash
   python your_script_name.py
   ```
   The script will:
   - Close any pop-ups if present.
   - Open the location map and check for availability at the test centre.
   - If available, book the test slot and notify you with a beep sound.
  
   Make sure you are on a DIFFERENT Location than the centre you want initially and then once on the booking page on the rsa website just run the script.

### Step 4: Configure and Re-run as Needed
If no slots are available, the script will wait for 30 seconds and then try again automatically. You can modify the wait time inside the `main()` function by changing the `time.sleep(30)` value.

## Customization

- **Retry Interval**: Change the retry time from 30 seconds to any value by modifying the `time.sleep()` parameter.
- **Notification Sound**: You can change the beep sound by modifying the `winsound.Beep(1000, 1000)` line to different frequency and duration values.

## Troubleshooting

- **WebDriver Issues**: If ChromeDriver is not working, ensure that it matches the version of Chrome you're using.
- **XPath Not Found**: Ensure that the XPaths/IDs are correct by using Chrome DevTools to inspect elements and find their paths.

---

### Example Code Snippet:

Replace the following placeholders in the code:

```python
# Example
modal_present = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, 'YOUR_MODAL_XPATH'))
)
```

Change `'YOUR_MODAL_XPATH'` to the actual XPath of the modal.

## Contributing

Feel free to submit issues or pull requests to improve the functionality or add new features!

---

This **README** provides a step-by-step guide for setting up, configuring, and running the script. 
