import requests
from datetime import datetime

from httpx import delete

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "asjkgtidpf385720^^"
USERNAME = "testusername01"

user_params = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#CREATING GRAPH
api_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"
GRAPHID = "mygraph"
graph_params = {
    "id": GRAPHID,
    "name": "Pushups Tracker",
    "unit": "Pushups",
    "type" : "int",
    "color": "kuro"
}

graph_header = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=api_endpoint, json=graph_params, headers=graph_header)
# print(graph_response.text)

#Creating a Pixel

add_pixel_endpoint = f"{api_endpoint}/{GRAPHID}"

#formatting date
today = datetime.now()
formatted_date = f'{today.strftime("%Y%m%d")}'

pixel_params = {
    "date" : "20250923",
    "quantity" : input("How many pushups did you do today?")
}

pixel_response = requests.post(url=add_pixel_endpoint,json=pixel_params, headers=graph_header)
print(pixel_response.text)

#UPDATING A PIXEL
update_pixel_endpoint = f"{add_pixel_endpoint}/{formatted_date}"
update_params = {
    "quantity" : "250"
}

# update_response = requests.put(url=update_pixel_endpoint, json=update_params, headers=graph_header)
# print(update_response.text)

#REMOVING A PIXEL
delete_pixel_endpoint = f"{add_pixel_endpoint}/{formatted_date}"
# delete_request = requests.delete(url=delete_pixel_endpoint, headers=graph_header)
# print(delete_request.text)
