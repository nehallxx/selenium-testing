# selenium-testing
# Selenium Python Scripts Documentation

This repository contains various Python scripts utilizing the Selenium library for web automation. Each script demonstrates different functionalities, from performing basic web interactions to handling more complex scenarios like coupon application and product data extraction.

## Prerequisites
- Install Python (>=3.6 recommended)
- Install Selenium: `pip install selenium`
- Download the appropriate WebDriver (e.g., ChromeDriver) and ensure it is in your system's PATH.

---

## Script Descriptions

### 1. **Basic Web Interactions (find_elements_test)**
- **Description**: Demonstrates navigation and interactions on the Demo Store website.
- **Features**:
  - Opens the homepage of `http://demostore.supersqa.com`.
  - Locates elements using `By.ID` and `By.CSS_SELECTOR`.
  - Searches for a product ("Hoodie") and navigates to the account section.

---

### 2. **Title and URL Validation (verify_link)**
- **Description**: Performs validation checks on the Python.org website.
- **Features**:
  - Opens `http://python.org`.
  - Validates the page title against an expected value.
  - Navigates to the PyPI section using `By.CSS_SELECTOR`.
  - Verifies the URL after navigation.

---

### 3. **Search and Element Visibility Check (verify_search)**
- **Description**: Conducts a search operation and verifies the visibility of search results.
- **Features**:
  - Opens `http://python.org`.
  - Searches for the term "testing".
  - Verifies the first result's link is displayed.
  - Uses `By.XPATH` and `By.ID` for locating elements.

---

### 4. **Cart Interaction and Coupon Application (verify_copoun)**
- **Description**: Automates adding items to a cart, applying a coupon, and verifying error messages on the Demo Store.
- **Features**:
  - Adds an item to the cart.
  - Navigates to the cart page.
  - Applies a coupon and checks for error messages.
  - Implements retry logic for verifying cart content.

---

### 5. **Product Data Extraction (scrape_price)**
- **Description**: Extracts product details from the Demo Store.
- **Features**:
  - Retrieves all products displayed on the homepage.
  - Extracts product names and prices using `By.CLASS_NAME` and `By.CSS_SELECTOR`.
  - Outputs the product information as a list of dictionaries.

---

## Usage Instructions

1. **Ensure the required dependencies are installed.**
   - Make sure you have Python installed and `selenium` installed via pip:
     ```bash
     pip install selenium
     ```
   - Download the appropriate WebDriver for your browser and place it in your system's PATH.

2. **Run the desired script using Python**:
   ```bash
   python script_name.py

