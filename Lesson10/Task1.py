from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Config import link, email_address, password, name, lastname

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    sign_in_button = browser.find_element(By.XPATH, "//*[@class='login']")
    sign_in_button.click()
    time.sleep(1)

    email_input = browser.find_element(By.XPATH, "//*[@id='email_create']")
    email_input.send_keys(email_address)
    time.sleep(1)

    submit_create_button = browser.find_element(By.XPATH, "//*[@id ='SubmitCreate']")
    submit_create_button.click()
    time.sleep(1)
    gender_button = browser.find_element(By.XPATH, "//*[@id ='id_gender1']")
    gender_button.click()
    firstname_field = browser.find_element(By.XPATH, "//*[@id ='customer_firstname']")
    lastname_field = browser.find_element(By.XPATH, "//*[@id ='customer_lastname']")
    password_field = browser.find_element(By.XPATH, "//*[@id ='passwd']")
    days_dropdown = Select(browser.find_element(By.XPATH, "//select[@id='days']"))
    months_dropdown = Select(browser.find_element(By.XPATH, "//select[@id='months']"))
    years_dropdown = Select(browser.find_element(By.XPATH, "//select[@id='years']"))
    submitAccountButton = browser.find_element(By.XPATH,"//button[@id='submitAccount']/span")

    firstname_field.send_keys(name)
    lastname_field.send_keys(lastname)
    password_field.send_keys(password)
    time.sleep(1)
    days_dropdown.select_by_value('3')
    months_dropdown.select_by_value('5')
    years_dropdown.select_by_value('2000')
    time.sleep(1)
    submitAccountButton.click()
    time.sleep(1)
    browser.get(link)
    time.sleep(1)
    sign_out_button = browser.find_element(By.XPATH, "//*[@class='logout']")
    sign_out_button.click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//*[@class='login']").click()
    time.sleep(1)
    submitLoginButton = browser.find_element(By.XPATH, "//button[@id='SubmitLogin']")
    email_field = browser.find_element(By.XPATH, "//input[@id='email']")
    email_field.send_keys(email_address)
    password_input = browser.find_element(By.ID, 'passwd')
    password_input.send_keys(password)
    time.sleep(1)
    submitLoginButton.click()
    time.sleep(1)

    browser.save_screenshot('result1.png')
finally:
    browser.quit()
