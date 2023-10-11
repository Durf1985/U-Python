# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta

# import os
# SHEET_USER = os.environ(SHEET_USER)
# SHEET_PASS = os.environ(SHEET_PASS)
ORIGIN_CITY_IATA = "LON"

flight_search = FlightSearch()

data_manager = DataManager()
sheet_data = data_manager.sheet_data

for record in sheet_data:
    if record["iataCode"] == '':
        data_manager.update_sheet_data(flight_search.get_city_list(sheet_data))
        break

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

pprint(sheet_data)

for record in sheet_data:

    flight = flight_search.check_flight(ORIGIN_CITY_IATA, record["iataCode"], from_time=tomorrow,
                                        to_time=six_month_from_today)
    if flight.price < record['lowestPrice']:
        data_manager.update_price(record, flight.price)

# TODO 1: переписать чарты, чтобы они качали свои зависимости с интернета, а не с локальной машины.
# TODO 2:
