from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_swag_workflow(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://saucedemo.com")
    assert "Swag Labs" in driver.title
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url
    dropdown = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
    select_element = Select(dropdown)
    select_element.select_by_value("lohi")
    price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    cleaned_prices = [float(item.text.replace("$", "")) for item in price_elements]
    assert cleaned_prices == sorted(cleaned_prices), f"Sorting is BROKEN! Got layout: {cleaned_prices}"

# to run the test:
## python -m pytest test_swag.py -s -v
