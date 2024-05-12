import csv
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from typing import List
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, hotels_list: List[WebElement]):
        self.hotels_list = hotels_list

    def pull_hotel_attributes(self):
        collection = []
        column_names = ["Hotel Name", "Price", "Score"]  # Define column names

        for hotel in self.hotels_list:
            try:
                hotel_name = hotel.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute(
                    'innerHTML').strip()
                hotel_price = hotel.find_element(By.CSS_SELECTOR,
                                                 'span[data-testid="price-and-discounted-price"]').get_attribute(
                    'innerHTML').strip()
                hotel_score = (
                    (((hotel.find_element(By.CSS_SELECTOR, 'div[data-testid="property-card-container"] .c1edfbabcb').
                       find_element(By.CLASS_NAME, 'b0db0e8ada')
                       .find_element(By.CLASS_NAME, 'f02fdbd759'))
                      .find_element(By.CSS_SELECTOR, 'a[data-testid="review-score-link"]'))
                     .find_element(By.CLASS_NAME, 'd86cee9b25'))
                    .find_element(By.TAG_NAME, 'div')).get_attribute('innerHTML').strip()
                collection.append(
                    [hotel_name, hotel_price, hotel_score]
                )
            except:
                pass

        # Save collection to a CSV file
        csv_file_path = "hotel_attributes.csv"
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(column_names)  # Write column names as the first row
            writer.writerows(collection)

        return collection
