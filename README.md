# Loblaws Product Scraping Bot

This Python bot scrapes product details from the [Loblaws Pantry page](https://www.loblaws.ca/food/pantry/c/28006?navid=flyout-L2-Pantry). It uses Selenium to extract product names and URLs, saving them in a CSV file. This bot is useful for anyone looking to analyze product data from Loblaws' pantry section.

## Features
- Scrolls through the Loblaws pantry section, scraping each product's name and link.
- Handles pagination by clicking the "Load More" button once a specific number of items have been scraped.
- Saves the data to a CSV file for easy access and analysis.

## Requirements
- Python 3.x
- Selenium WebDriver
- ChromeDriver (compatible with your Chrome version)

### Install Python Packages
Ensure that you have Selenium installed:
```bash
pip install selenium
