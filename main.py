##########################################################################################
# Step 1: Configure and Start the Browser
##########################################################################################

# 1: Use the WebDriver class to define a ChromeOptions object named options.
from selenium import webdriver
options = webdriver.ChromeOptions()

# 2: Add the "start-maximized" argument to the options for fullscreen mode.
options.add_argument("--start-maximized")

# 3: Create a Chrome driver using the previously defined options.
driver = webdriver.Chrome(options)


##########################################################################################
# Step 2: Analyzing and Scraping the Home Page
##########################################################################################

# 1: Open and inspect the homepage using the driver.
import time
SLEEP_TIME = 2

driver.get("https://books.toscrape.com/")
time.sleep(SLEEP_TIME)

# 2: Write the XPath query to find elements that contain the links for "Travel" and "Nonfiction" categories.
category_elements_xpath = "//a[contains(text(), 'Travel') or contains(text(), 'Nonfiction')]"

# 3: Use the XPath query to find the elements with driver and extract the category links.
from selenium.webdriver.common.by import By
category_elements = driver.find_elements(By.XPATH, category_elements_xpath)

category_urls = [element.get_attribute("href") for element in category_elements]
print(category_urls)


#######################################################################
# Step 3: Analyzing and Scraping the Category Page
######################################################################

# 1: Enter any category detail page and write the XPath query for elements that contain the book detail links.
driver.get(category_urls[0])
time.sleep(SLEEP_TIME)
book_elements_xpath = "//div[@class='image_container']//a"

# 2: Use the driver to find elements with the XPath query and extract the detail links.
book_elements = driver.find_elements(By.XPATH, book_elements_xpath)
book_urls = [element.get_attribute("href") for element in book_elements]
print(book_urls)
print(len(book_urls))


# 3: Instead of clicking pagination buttons, manipulate the page link and use a loop to handle pagination.
# Tip: Observe how the URL changes as you switch pages.
MAX_PAGINATION = 3
url = category_urls[0]
book_urls = []
for i in range(1, MAX_PAGINATION):
    update_url = url if i == 1 else url.replace("index", f"page-{i}")
    driver.get(update_url)
    book_elements = driver.find_elements(By.XPATH, book_elements_xpath)

    temp_urls = [element.get_attribute("href") for element in book_elements]
    book_urls.extend(temp_urls)

print(book_urls)
print(len(book_urls))


# 4: To check if you've reached the last page of pagination, go to the 999th page of the category and inspect the page.
# Tip: ..../category/books/nonfiction_13/page-999.html


# 5: To avoid infinite loops in pagination, check for a page that contains a 404 error or verify the presence of book elements.
# Tip: Check if there's an h1 tag containing the text "404" or (if not book_elements) or (len(book_elements) <= 0).

MAX_PAGINATION = 3
url = category_urls[0]
book_urls = []
for i in range(1, MAX_PAGINATION):
    update_url = url if i == 1 else url.replace("index", f"page-{i}")
    driver.get(update_url)
    book_elements = driver.find_elements(By.XPATH, book_elements_xpath)
    if not book_elements:
        break

    temp_urls = [element.get_attribute("href") for element in book_elements]
    book_urls.extend(temp_urls)

print(book_urls)
print(len(book_urls))


###############################################
# Step 4: Scraping the Product Detail Page
###############################################

# 1: Go to any product detail page and find the div element with the class attribute 'content'.
driver.get(book_urls[0])
time.sleep(SLEEP_TIME)
content_div = driver.find_elements(By.XPATH, "//div[@class='content']")

# 2: Get the inner HTML of the div element and assign it to the variable inner_html.
inner_html = content_div[0].get_attribute("innerHTML")

# 3: Create a BeautifulSoup object using the inner_html.
from bs4 import BeautifulSoup
soup = BeautifulSoup(inner_html, "html.parser")

# 4: Using the soup object, scrape the following information:
# ▪ Book Title
name_elem = soup.find("h1")
book_name = name_elem.text

# ▪ Book Price
price_elem = soup.find("p", attrs={"class": "price_color"})
book_price = price_elem.text

# ▪ Book Star Rating
# Tip: ( regex = re.compile('^star-rating '))
import re
regex = re.compile('^star-rating ')
star_elem = soup.find("p", attrs={"class": regex})
book_star_count = star_elem["class"][-1]

# ▪ Book Description
desc_elem = soup.find("div", attrs={"id": "product_description"}).find_next_sibling()
book_desc = desc_elem.text

# ▪ Product Information under the "Product Information" heading.
product_info = {}
table_rows = soup.find("table").find_all("tr")
for row in table_rows:
    key = row.find("th").text
    value = row.find("td").text
    product_info[key] = value



