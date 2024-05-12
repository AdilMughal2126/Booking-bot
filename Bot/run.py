from booking.Booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency()
    bot.select_place_to_go('New York')
    bot.select_dates('2024-05-15', '2024-05-20')
    bot.select_occupancy(10)
    bot.click_search()
    bot.apply_filtration()
    bot.report_results()
