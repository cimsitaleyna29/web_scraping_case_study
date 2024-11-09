# Web Scraping for Competitor and Price Analysis

This project aims to scrape detailed information about books in the "Travel" and "Nonfiction" categories from the website [https://books.toscrape.com/](https://books.toscrape.com/). The goal is to conduct competitor and price analysis for these categories to help an online bookstore improve its sales.

## Project Overview

An online bookstore has noticed that the "Travel" and "Nonfiction" categories are not generating the expected sales. The company wants to gather more information about the pricing strategies and product details of its competitors. This project will scrape data from the mentioned website to provide the necessary information for competitor analysis and price comparison.

## Project Workflow

### 1. Category Link Extraction:
- Extract the URLs of the "Travel" and "Nonfiction" categories from the homepage.

### 2. Access Product Detail Pages:
- Visit the category pages and scrape the links to all product detail pages for books in those categories.

### 3. Scrape Book Information:
For each book, scrape the following information:
- Book Title
- Price
- Star Rating
- Description
- Product Information (e.g., product specifications)

### 4. Analysis:
- The collected data can be used for competitor analysis and price comparison.

## Technologies Used

- **Selenium:** Used to automate browser actions and scrape dynamic content.
- **BeautifulSoup:** Used for HTML parsing and extracting specific data from web pages.
- **Python:** The primary programming language used for writing the web scraping scripts.
