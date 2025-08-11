from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Auto-manage ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Open Flipkart
driver.get("https://www.flipkart.com/")
time.sleep(2)

#Close login popup
try:
    close_button = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
    close_button.click()
except:
    pass

# Search for a product
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Prepare lists
titles, prices, ratings = [], [], []

products = driver.find_elements(By.XPATH, "//div[@class='_1AtVbE']")

for product in products:
    try:
        title = product.find_element(By.CLASS_NAME, "_4rR01T").text
        price = product.find_element(By.CLASS_NAME, "_30jeq3").text
        try:
            rating = product.find_element(By.CLASS_NAME, "_3LWZlK").text
        except:
            rating = "No Rating"
        titles.append(title)
        prices.append(price)
        ratings.append(rating)
    except:
        continue

driver.quit()

# Save to CSV
df = pd.DataFrame({"Title": titles, "Price": prices, "Rating": ratings})
df.to_csv("products.csv", index=False)

print("Data saved to products.csv")



