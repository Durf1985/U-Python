import requests
from pprint import pprint
import os


class DataManager:

    def __init__(self):
        # self.end_point = os.environ(SHEET_END_POINT)
        # self.user = os.environ(SHEET_USER)
        # self.password = os.environ(SHEET_PASS)

        self.end_point = "https://api.sheety.co/8153e6a5fe4974db9df23214e6e642ce/myFlightDeals/prices/"
        self.user = "durf"
        self.password = "EKG!Ks9H1*a4*Cy2"
        self.sheet_data = self.get_sheet_data()

    def get_sheet_data(self):
        response = requests.get(url=self.end_point, auth=(self.user, self.password))
        response.raise_for_status()
        result = response.json()
        return result['prices']

    def update_sheet_data(self, sheet_data: list):
        for record in sheet_data:
            upd_data = {
                "price": {
                    "city": record["city"],
                    "iataCode": record["iataCode"],
                    "id": record["id"],
                    "lowestPrice": record["lowestPrice"]
                }
            }
            update = requests.put(url=f"{self.end_point}/{record['id']}", json=upd_data,
                                  auth=(self.user, self.password))
            update.raise_for_status()

    def update_price(self, sheet_data, update):
        pprint(sheet_data)

        upd_data = {
            "price": {
                "city": sheet_data["city"],
                "iataCode": sheet_data["iataCode"],
                "id": sheet_data["id"],
                "lowestPrice": update
            }
        }
        update = requests.put(url=f"{self.end_point}/{sheet_data['id']}", json=upd_data,
                              auth=(self.user, self.password))
        update.raise_for_status()
