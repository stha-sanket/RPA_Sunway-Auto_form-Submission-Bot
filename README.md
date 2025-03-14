# Sunway Contact Form Filler

## Description

This Robocorp script automates filling out and submitting the contact form on the Sunway International Business School website.

## Prerequisites

*   **Python 3.7+**
*   **Robocorp Framework**
*   **Required Libraries**:
    *   `rpaframework`
    *   `rpaframework-browser`
*   Install these libraries using the Vs-code extension
*   ![Requirement Extension](https://github.com/stha-sanket/RPA-Auto-WebsiteScraper/blob/main/requirement-extension.png?raw=true)

## Setup and Installation

1.  **Install Robocorp Framework:**
    ```bash
    pip install robocorp-framework
    ```

2.  **Install Required Libraries:**
    ```bash
    pip install rpaframework rpaframework-browser
    ```

## Usage

1.  **Run the Robot:**

    Navigate to the directory containing the robot script (e.g., `sunway_contact.py`) and run:

    ```bash
    rcc task run
    ```

    This command will execute the `robot_spare_bin_python` task.

## Code Explanation

*   **Robocorp Framework:** Provides the structure for defining and running tasks.
*   **Browser Library:** Controls the web browser (Chromium) for navigating the Sunway website and interacting with the contact form.

## Task Breakdown

*   `robot_spare_bin_python()`: The main task function that orchestrates the entire process.
    *   Configures browser settings (slow motion for easier debugging).
    *   Calls the `open_the_sunway_website` function to navigate to the website.
    *   Calls the `fill_contact_form` function to fill in the contact form fields.
    *   Calls the `submit_form` function to submit the form.
*   `open_the_sunway_website()`: Navigates the browser to the Sunway International Business School website's homepage.
*   `fill_contact_form()`: Locates the contact form fields on the page using XPath expressions and fills them with predefined values (e.g., "John Doe" for the name, "johndoe@example.com" for the email). The function also waits for each element to load using `page.wait_for_selector`.
*   `submit_form()`: Locates the "Send Message" button on the page using an XPath expression and clicks it to submit the form.  The function also waits for the button to load using `page.wait_for_selector`.

## Important Considerations

*   **Website Stability:** The script relies heavily on XPath expressions.  Any changes to the Sunway website's HTML structure, especially the structure of the contact form, will likely break the script.
*   **XPath Locators:** The script uses XPath expressions for locating form elements. These XPaths can be fragile and may change if the website's HTML structure is updated.  Always use the browser's developer tools to inspect the HTML and verify the XPaths before running the script. **It is highly recommended to use more reliable locators such as `id`, `name`, or CSS selectors whenever possible.** XPaths like `//*[@id='wpcf7-f6-o2']/form/p[1]/span/input` are very specific and likely to break.
*   **`wait_for_selector` Timeouts:** The script uses `page.wait_for_selector` with a timeout to wait for elements to load.  The default timeout is large (1800000 ms = 30 minutes for the first element). You should adjust these timeouts as needed based on your network speed and the website's loading time. Shorter timeouts will make the script run faster if elements load quickly, but may cause the script to fail if elements take longer to load.  Consider reducing these timeouts and adding more robust error handling.
*   **Predefined Values:** The script uses predefined values for the contact form fields. You can modify these values in the `fill_contact_form` function to use different information.
*   **Submission Success:** The script does not currently verify whether the form submission was successful.  You could add code to check for a success message on the page after submitting the form.
*   **`slowmo`**: The line `browser.configure(slowmo=100)` adds a small delay (100 milliseconds) after each browser action. This can make the script easier to debug, but slows down the overall execution. Remove or reduce the `slowmo` value to make the script run faster.

## Potential Improvements

*   **More Robust Locators:** Replace XPath expressions with more robust locators, such as CSS selectors or element IDs, whenever possible.
*   **Configuration File:** Use a configuration file to store the website URL, contact form field values, and other settings.
*   **Submission Verification:** Add code to verify whether the form submission was successful by checking for a success message on the page.
*   **Error Handling:** Implement more comprehensive error handling to catch potential exceptions and provide informative error messages.
*   **Data Validation:** Add data validation to ensure that the contact form field values are in the correct format.
*   **Captcha Handling:** If the website uses a CAPTCHA, you will need to implement a CAPTCHA solving mechanism. This can be a complex task and may require the use of third-party services.  Solving CAPTCHAs is often against the terms of service of the website.
*   **Headless Mode:** Run the browser in headless mode (without a visible browser window) to improve performance. This can be done by adding appropriate browser launch options.
