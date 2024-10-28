import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = "https://www.loblaws.ca/food/pantry/c/28006?navid=flyout-L2-Pantry"

# make sure to add your chromedriver.exe file in C:/ (or update the path)
driver = webdriver.Chrome("C:/chromedriver")

driver.get(url)
driver.implicitly_wait(20)
elements = driver.find_elements(By.CLASS_NAME, value='product-tile__details__info__name__link')
print(len(elements))
i = 0
counter = 1
f = open('D:\\Fiverr\\05-23-2023\\data.csv', 'w', newline='')
writer = csv.writer(f)
failed_count = 0
while True:
    try:
        driver.implicitly_wait(10)
        title = driver.find_element(By.XPATH, value=f'(//a[@class="product-tile__details__info__name__link"])[{counter}]')
        driver.execute_script("arguments[0].scrollIntoView();", title)
        title = title.text
        url = driver.find_element(By.XPATH,
                                  value=f'(//a[@class="product-tile__details__info__name__link"])[{counter}]').get_attribute('href')
        i += 1
        counter += 1
        writer.writerow([title, url])
        if i == 47:
            load_button = driver.find_element(By.CSS_SELECTOR, value='div[class="load-more-button"] button')
            driver.execute_script("arguments[0].scrollIntoView();", load_button)
            time.sleep(2)
            driver.execute_script("arguments[0].click();", load_button)
            print('clicked')
            i = 0
            print('sleeping for 5 seconds')
            time.sleep(3)


    except:
        failed_count += 1
        if failed_count == 20:
            break
        print('failed   ------------ ', failed_count)