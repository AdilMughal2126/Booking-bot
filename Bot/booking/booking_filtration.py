from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        for star_value in star_values:
            print(f'div[data-filters-item="class:class={star_value}"]')
            star_element = self.driver.find_element(By.CSS_SELECTOR,
                                                    f'div[data-filters-item="class:class={star_value}"]')
            star_element.click()
