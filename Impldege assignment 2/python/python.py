from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Function to generate a random integer less than 20
def generate_random_dimension():
    return random.randint(1, 20)

# Function to handle test case 01: Add Package
def test_case_01(driver):
    try:
        # Step 01: Login to the application
        driver.get("https://ecs-qa.kloudship.com")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
        driver.find_element(By.ID, "email").send_keys("kloudship.qa.automation@mailinator.com")
        driver.find_element(By.ID, "password").send_keys("Password1")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Step 02: Navigate to Package Types
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Package Types"))).click()

        # Step 03: Click on Add Manually button
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Add Manually')]"))).click()

        # Step 04: Add a package
        package_name = "FirstName_LastName"
        package_dimensions = generate_random_dimension()

        driver.find_element(By.ID, "name").send_keys(package_name)
        driver.find_element(By.ID, "dimensions").send_keys(str(package_dimensions))

        # Step 05: Submit the form
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Step 06: Logout the application
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Logout"))).click()
    except Exception as e:
        print(f"An error occurred during Test Case 01: {e}")

# Function to handle test case 02: Delete Package
def test_case_02(driver):
    try:
        # Step 01: Login to the application
        driver.get("https://ecs-qa.kloudship.com")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
        driver.find_element(By.ID, "email").send_keys("kloudship.qa.automation@mailinator.com")
        driver.find_element(By.ID, "password").send_keys("Password1")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Step 02: Navigate to Package Types
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Package Types"))).click()

        # Step 03: Delete the newly added package
        package_name = "FirstName_LastName"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//td[contains(text(),'{package_name}')]/following-sibling::td/a"))).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='button']"))).click()

        # Step 04: Logout the application
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Logout"))).click()
    except Exception as e:
        print(f"An error occurred during Test Case 02: {e}")

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# Execute Test Case 01
test_case_01(driver)
time.sleep(3)  # Wait for changes
