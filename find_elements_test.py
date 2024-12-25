from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com")
# By ID for Cart
cart=driver.find_element(By.ID,"site-header-cart")
print(cart)
print(type(cart))
# ---------------------

# By ID Type Search
search_field=driver.find_element(By.ID, "woocommerce-product-search-field-0")
search_field.send_keys("Hoodie")
search_field.send_keys(Keys.ENTER)
# ---------------------

# By CSS Selector select Account
my_acc=driver.find_element(By.CSS_SELECTOR, "#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9.focus > a")
my_acc.click()