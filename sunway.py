from robocorp.tasks import task
from robocorp import browser

@task
def robot_spare_bin_python():
    """Fills out the contact form on the Sunway website"""
    browser.configure(
         slowmo=100,
    )
    open_the_sunway_website()
    fill_contact_form()
    submit_form()

def open_the_sunway_website():
    """Navigates to the Sunway contact page"""
    page = browser.page()
    page.goto("https://sunway.edu.np/", timeout=1200000)

def fill_contact_form():
    """Fill the contact form fields"""
    page = browser.page()

    page.wait_for_selector("//*[@id='wpcf7-f6-o2']/form/p[1]/span/input", timeout=1800000)
    page.fill("//*[@id='wpcf7-f6-o2']/form/p[1]/span/input", "John Doe")

    page.wait_for_selector("//*[@id='wpcf7-f6-o2']/form/p[2]/span/input", timeout=60000)
    page.fill("//*[@id='wpcf7-f6-o2']/form/p[2]/span/input", "johndoe@example.com")

    page.wait_for_selector('//*[@id="wpcf7-f6-o2"]/form/p[3]/span/div/input[1]', timeout=60000)
    page.fill( '//*[@id="wpcf7-f6-o2"]/form/p[3]/span/div/input[1]', "9800000000")

    page.wait_for_selector('//*[@id="wpcf7-f6-o2"]/form/p[4]/span/input', timeout=60000)
    page.fill('//*[@id="wpcf7-f6-o2"]/form/p[4]/span/input', "Inquiry")

    page.wait_for_selector('//*[@id="wpcf7-f6-o2"]/form/p[5]/span/textarea', timeout=60000)
    page.fill('//*[@id="wpcf7-f6-o2"]/form/p[5]/span/textarea', "Hello, I have an inquiry about your services.")

def submit_form():
    """Clicks the 'Send Message' button"""
    page = browser.page()
    page.wait_for_selector('//*[@id="wpcf7-f6-o2"]/form/p[6]/button', timeout=60000)
    page.click('//*[@id="wpcf7-f6-o2"]/form/p[6]/button')
