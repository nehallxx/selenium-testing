from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("http://python.org")

curr_title=driver.title
expect_title="Welcome to Python.org"
if curr_title !=expect_title:
    raise Exception("not the same title, current title is : {}".format(curr_title))

pypi_header='#top > nav > ul > li.pypi-meta > a'
pypi_header_ele=driver.find_element(By.CSS_SELECTOR, pypi_header)
pypi_header_ele.click()

curr_url=driver.current_url
expect_url='https://pypi.org/'
assert curr_url==expect_url, f"url opened is: {curr_url}"
print("PASS")
