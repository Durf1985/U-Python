import requests
from datetime import datetime

endpoint = "https://pixe.la/v1/users"
USER = "durf"
TOKEN = "alsjdhfldsjfuerofjghsl"
ID = "graph1"
user_param = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=endpoint, json=user_param)
# print(response.text)

graph_end = f"{endpoint}/{USER}/graphs"

graph_conf = {
    "id": ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# graph_response = requests.post(url=graph_end, json=graph_conf, headers=headers)
# print(graph_response.text)


pixel_end = f"{endpoint}/{USER}/graphs/{ID}"
d = datetime.now().strftime("%Y%m%d")
print(d)
pixel_param = {
    "date": d,
    "quantity": "5.1",
}

# pixel_resp = requests.post(url=pixel_end, json=pixel_param, headers=headers)

# print(pixel_resp.text)

pixel_end_update = f"{pixel_end}/{d}"

update = {
    "quantity": "25.0"
}

# response = requests.put(url=pixel_end_update, json=update, headers=headers)

# print(response.text)

response = requests.delete(url=pixel_end_update, headers=headers)
