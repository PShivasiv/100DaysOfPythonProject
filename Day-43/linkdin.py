ACCOUNT_PASSWORD = "#YOUR PASSWORD"




from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = "siv23shiva@gmail.com"
PHONE = "9873810930"


chrom_option = webdriver.ChromeOptions()
chrom_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrom_option)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3937594990&f_AL=true&geoId=102713980&keywords=python%20developer%20fresher&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&spellCorrectionEnabled=true")


# job_title = driver.find_element(By.CSS_SELECTOR, value=".full-width artdeco-entity-lockup__title ember-view a")
# easy_apply = driver.find_element(By.CSS_SELECTOR,value=".jobs-apply-button--top-card button")
# next = driver.find_element(By.CSS_SELECTOR,value=".display-flex justify-flex-end ph5 pv4 button")
# next2 = driver.find_element(By.CSS_SELECTOR,value=" .display-flex justify-flex-end ph5 pv4 .artdeco-button artdeco-button--2 artdeco-button--primary ember-view")
# review = driver.find_element(By.ID,value="ember363")
# submit = driver.find_element(By.ID,value="ember373")


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


#sign in account 
time.sleep(2)
sign = driver.find_element(By.XPATH,value="/html/body/div[2]/a[1]")
sign.click()

#Enter the email and password

user_id = driver.find_element(By.XPATH, value='//*[@id="username"]')
password = driver.find_element(By.XPATH, value='//*[@id="password"]')
user_id.send_keys(ACCOUNT_EMAIL)
password.send_keys(ACCOUNT_PASSWORD)
time.sleep(4)
sign_in = driver.find_element(By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()
time.sleep(5)

#get lisitings 
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".jobs-search-results-list ul  li div a")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(5)
    # click to easy apply 
    try:
        easy_apply = driver.find_element(By.CSS_SELECTOR,value=".jobs-apply-button--top-card button")
        if easy_apply.text == "Easy Apply":
            easy_apply.click()
            time.sleep(5)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()
        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except:
        abort_application()
        print("No application button, skipped.")
        continue
        
driver.quit()
time.sleep(2)
