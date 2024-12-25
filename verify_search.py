from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://python.org")
driver.implicitly_wait(10)

curr_title=driver.title
expect_title="Welcome to Python.org"
if curr_title !=expect_title:
    raise Exception("not the same title, current title is : {}".format(curr_title))

search_box=driver.find_element(By.ID,"id-search-field")
search_box.send_keys("testing")
go_btn=driver.find_element(By.ID,"submit")
go_btn.click()

first_link_xpath='//*[@id="content"]/div/section/form/ul/li[1]/h3/a'
first_link_ele=driver.find_element(By.XPATH,first_link_xpath)
# import pdb; pdb.set_trace()

if first_link_ele.is_displayed():
    print("PASS")
else:
    raise Exception("not displayed")

driver.quit()