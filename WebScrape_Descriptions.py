from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

#Navigate to a webpage
driver.get('https://www.bls.gov/ooh/a-z-index.htm')

#Get browser information
#driver.title
#driver.current_url

careers = ['Lawyers', "Mechanical engineers"]

for career in careers:
    try:
        link = driver.find_element(By.LINK_TEXT, career)

        link.click()

        time.sleep(3)

        summary = driver.find_element(By.CSS_SELECTOR, 'div#tab-1')
        summary_text = summary.text

        print(f"\nSummary for {career}:({driver.current_url}):\n")
        print(summary_text)

        driver.get('https://www.bls.gov/ooh/a-z-index.htm')
        time.sleep(3)

    except Exception as e:
        print(e)

driver.quit()