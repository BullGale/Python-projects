import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
username = "jeet"
token = "mnfe5wfe2313ad1dadas1d"

user_param = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_id = "graph1"

graph_config = {
    "id": graph_id,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji"
}

header = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

px_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

today = datetime(year=2022, month=6, day=17)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? ")
}

response = requests.post(url=px_creation_endpoint, json=pixel_data, headers=header)
print(response.text)

px_update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"

update_data = {
    "quantity": "10.5"
}

# response = requests.put(url=px_update_endpoint, json=update_data, headers=header)
# print(response.text)

px_delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=px_delete_endpoint, headers=header)
# print(response.text)