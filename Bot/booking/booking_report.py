from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from typing import List
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, hotels_list: List[WebElement]):
        self.hotels_list = hotels_list

    def pull_hotel_attributes(self):
        collection = []
        for hotel in self.hotels_list:
            hotel_name = hotel.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute(
                'innerHTML').strip()
            hotel_price = hotel.find_element(By.CSS_SELECTOR,
                                             'span[data-testid="price-and-discounted-price"]').get_attribute(
                'innerHTML').strip()
            # hotel_score = hotel.find_element(By.CSS_SELECTOR, 'a[target="_blank"] div[data-testid="review-score"]')
            collection.append(
                [hotel_name, hotel_price]
            )

        return collection
