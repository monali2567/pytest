from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
@pytest.mark.great

def test_new_tab_a():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://demoqa.com/browser-windows")
    main_page=driver.current_window_handle
    print(main_page)
    time.sleep(3)
    newtab=driver.find_element(By.ID,"tabButton")
    newtab.click()
    print(driver.window_handles)
    for handle in driver.window_handles:
        if handle != main_page:
            ntab = handle
        driver.switch_to.window(ntab)
        time.sleep(3)
        print(driver.current_window_handle)
        time.sleep(3)
        driver.switch_to.window(main_page)
        time.sleep(3)
        print(driver.current_window_handle)
    print(driver.title)
    # title = "Sample page - lambdatest.com"
    # assert title == driver.title
    driver.close()
@pytest.mark.great    
@pytest.mark.win
def test_new_window_b():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://demoqa.com/browser-windows")
    main_page=driver.current_window_handle
    print(main_page)
    time.sleep(3)
    driver.find_element(By.ID,"windowButton").click()
    for handle in driver.window_handles:
        if handle != main_page:
            nwindow = handle
    print(nwindow)
    driver.switch_to.window(nwindow)

    h=driver.find_element(By.ID,"sampleHeading")
    print(h.text)
    time.sleep(3)
    driver.switch_to.window(main_page)
    print(main_page)

    driver.close()
