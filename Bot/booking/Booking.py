from . import booking_filtration
from . import constants
from . import booking_report
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"c:/seleniumDrivers/chromedriver-win64/chromedriver.exe", teardown=False):
        options = Options()
        options.add_argument("--remote-debugging-port=9222")  # Use an arbitrary port number
        options.add_experimental_option("detach", True)  # Keep the browser window open after exiting the sc

        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(url=constants.BASE_URL)

    def change_currency(self, currency=None):
        self.remove_popup_if_present()
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()

        selected_currency = self.find_element(By.CSS_SELECTOR, 'button.ac7953442b')
        selected_currency.click()

    def remove_popup_if_present(self):
        try:
            pop_up_close_element = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]'
            )
            pop_up_close_element.click()
        except:
            print('Pop up not occur...resuming')

    def select_place_to_go(self, place_to_go):
        self.remove_popup_if_present()

        search_field = self.find_element(By.CSS_SELECTOR, 'input[name="ss"]')
        search_field.clear()
        search_field.send_keys(place_to_go)
        self.remove_popup_if_present()

        first_search_result = self.find_element(
            By.ID, 'autocomplete-result-0'
        )

        first_search_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def select_occupancy(self, adult_count):
        occupancy_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]'
        )
        occupancy_element.click()

        while True:
            decrease_element = self.find_element(
                By.CSS_SELECTOR, 'button.e91c91fa93'
            )

            decrease_element.click()

            increase_element = self.find_element(
                By.CSS_SELECTOR, 'button.f4d78af12a'
            )

            adults_value_element = self.find_element(
                By.ID, 'group_adults'
            )

            adult_count_value = adults_value_element.get_attribute('value')

            for count in range(adult_count - 1):
                increase_element.click()

            if int(adult_count_value) == 1:
                break

    def click_search(self):
        search_element = self.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        )

        search_element.click()

    def apply_filtration(self):
        filtration = booking_filtration.BookingFiltration(driver=self)
        self.remove_popup_if_present()
        filtration.apply_star_rating(3, 4, 5)

    def report_results(self):
        hotel_boxes = self.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
        report = booking_report.BookingReport(hotel_boxes)
        table = PrettyTable(field_names=["Hotel Name", "Hotel Price"])
        table.add_rows(report.pull_hotel_attributes())
        print(table)
