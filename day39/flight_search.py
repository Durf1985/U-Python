# This class is responsible for talking to the Flight Search API.
# import os
import requests
from flight_data import FlightData

from pprint import pprint


class FlightSearch:
    def __init__(self):
        # self.fligth_search_end = os.environ("FLIGHT_SEARCH_LOCATION_ENDPOINT")
        # self.fligth_search_api_key = os.environ("FLIGHT_SERACH_API_KEY")
        self.endpoint = "https://api.tequila.kiwi.com"
        self.fligth_search_api_key = "aznp6weScUMB9Jb0pbYrPi8PHFNTLuBi"

    def get_city_list(self, sheet_data: list):
        for record in sheet_data:
            if record["iataCode"] == '':
                record["iataCode"] = self.search_city_code(record["city"])
        return sheet_data

    def search_city_code(self, city_name: str):
        parametr = {
            "term": city_name
        }
        header = {
            "apikey": self.fligth_search_api_key
        }
        response = requests.get(url=f"{self.endpoint}/locations/query", params=parametr, headers=header)
        response.raise_for_status()
        result = response.json()
        for x in result["locations"]:
            if 'city' in x:
                return (x['city']['code'])

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apikey": self.fligth_search_api_key
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=f"{self.endpoint}/v2/search", params=query, headers=headers)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
