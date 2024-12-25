from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://demostore.supersqa.com")

all_products=driver.find_elements(By.CLASS_NAME, "product-type-simple")
prod_info=[]
print(f"Number of products is: {len(all_products)}")

for product in all_products:
  ele_price=product.find_element(By.CSS_SELECTOR,"span.amount")
  price=ele_price.text
  ele_name=product.find_element(By.CSS_SELECTOR,"h2.woocommerce-loop-product__title")
  name=ele_name.text
  print(price)
  print(name)
  prod_info.append({"name": name, "price": price})
print(prod_info)
