from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def open_browser():
  driver=webdriver.Chrome()
  driver.implicitly_wait(10)
  return driver

def go_to_home_page(driver):
    driver.get("http://demostore.supersqa.com")

def add_item_to_cart(driver):
    add_btn=driver.find_element(By.CLASS_NAME,'add_to_cart_button')
    add_btn.click()

def go_to_cart_page(driver):
    driver.get("http://demostore.supersqa.com/cart")

def apply_coupon(driver, coupon):
    coupon_field = driver.find_element(By.ID, "coupon_code")
    coupon_field.send_keys(coupon)
    apply_btn = driver.find_element(By.CSS_SELECTOR, "#post-7 > div > div > form > table > tbody > tr:nth-child(2) > td > div > button")
    apply_btn.click()


def verify_cart(driver):
    for i in range(5):
        try:
            driver.find_element(By.ID,"cart-item")
            return
        except NoSuchElementException:
            print("Item not found, retrying in 2 sec...")
            time.sleep(2)
            driver.refresh()

def display_err_msg(driver):
    return driver.find_element(By.XPATH, '//*[@id="post-7"]/div/div/div[1]/ul/li').text




if __name__== '__main__':
    driver=open_browser()
    go_to_home_page(driver)
    add_item_to_cart(driver)
    go_to_cart_page(driver)
    verify_cart(driver)
    apply_coupon(driver, 'fakeone')
    display_err_msg(driver)
    expect_msg=display_err_msg(driver)
    curr_msg='Coupon "fakeone" does not exist!'
    assert expect_msg==expect_msg, f"Unexpected msg: {expect_msg}"
    print("PASS")
