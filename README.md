# eBay Laptop Scraper

## Description

This Robocorp script scrapes laptop listings from eBay, extracting the product name, price, and product link, and saves the data into a CSV file.

## Prerequisites

*   **Python 3.7+**
*   **Robocorp Framework**: `pip install robocorp-framework`
*   **Required Libraries**:
    *   `rpaframework`
    *   `rpaframework-browser`
    *   `lxml`
*   Install these libraries using `pip install rpaframework rpaframework-browser lxml`

## Setup and Installation

1.  **Install Robocorp Framework:**
    ```bash
    pip install robocorp-framework
    ```

2.  **Install Required Libraries:**
    ```bash
    pip install rpaframework rpaframework-browser lxml
    ```

## Usage

1.  **Run the Robot:**

    Navigate to the directory containing the robot script (`rpa_script.py`) and run:

    ```bash
    rcc task run
    ```

    This command will execute the `robot_spare_bin_python` task.

## Code Explanation

*   **Robocorp Framework:** Provides the structure for defining and running tasks.
*   **Browser Library:** Controls the web browser (Chromium) for navigating the eBay website and extracting data.
*   **`lxml`:** Parses the HTML content of the eBay page to efficiently extract data using XPath expressions.
*   **CSV Library (built-in):** Used to write the scraped data to a CSV file.

## Task Breakdown

*   `robot_spare_bin_python()`: The main task function that orchestrates the entire scraping process.
    *   Configures browser settings (slow motion for easier debugging).
    *   Opens the CSV file for writing.
    *   Calls the `scrape_ebay_laptops` function to perform the scraping.
*   `scrape_ebay_laptops(url, writer)`: Scrapes laptop information from the given eBay URL.
    *   Navigates to the specified URL.
    *   Gets the page content.
    *   Uses `lxml` to parse the HTML content and extract data using XPath expressions.
    *   Iterates through each product listing, extracting the title, price, and link.
    *   Writes the extracted data to the CSV file.

## Output

The script produces the following output file:

*   `ebay_laptops.csv`: A CSV file containing the scraped laptop data, including the product name, price, and link.  It will overwrite the file if it exists.

## Important Considerations

*   **eBay's HTML Structure:** The script relies on the specific HTML structure of the eBay website. Changes to eBay's layout or class names may cause the script to fail. You'll need to update the XPath expressions in the `scrape_ebay_laptops` function if eBay's HTML changes. Use your browser's developer tools to inspect the HTML and find the appropriate XPath expressions.
*   **Website Terms of Service:** Be aware of eBay's terms of service regarding web scraping. Avoid making excessive requests or scraping data that is not publicly available.
*   **User-Agent:** Consider setting a custom User-Agent in the `browser.configure` to avoid being blocked by eBay.
*   **Error Handling:** The script includes basic error handling (e.g., checking if the title, price, and link exist). You can add more robust error handling to handle other potential issues, such as network errors or invalid data.
*   **Rate Limiting:**  The script could be improved by implementing rate limiting (adding delays between requests) to avoid overloading eBay's servers and potentially getting blocked.
*   **Dynamic Content:** If eBay uses JavaScript to load product information dynamically, the script might not be able to scrape all the data. In such cases, you might need to use more advanced techniques, such as waiting for elements to load or executing JavaScript code within the browser.
*   **`slowmo`**:  The line `browser.configure(slowmo=50)` adds a short delay (50 milliseconds) after each browser action. This can make the script easier to debug, but slows down the overall execution.  Remove or reduce the `slowmo` value to make the script run faster.

## Potential Improvements

*   **Configuration:** Add a configuration file to store the eBay URL and CSV file name.
*   **Pagination:** Implement pagination to scrape multiple pages of laptop listings.
*   **User Input:** Allow users to specify search keywords through command-line arguments or a configuration file.
*   **Logging:** Add logging to track the script's progress and any errors that occur.
*   **Filters:**  Implement filters to scrape only specific types of laptops (e.g., based on price, brand, or features).
*   **Robust Error Handling:**  Implement more comprehensive error handling to catch potential exceptions and provide informative error messages.  This should include checking the HTTP status code after navigating to the URL.
