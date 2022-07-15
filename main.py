import requests
from datetime import datetime

username="Enter user pixela Username"
token="Enter user pixela token / api key"
graph_id="demograph"
pixela_end_point="https://pixe.la/v1/users"


user_param={
    "token":token, 
    "username":username, 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
    }

# responses=requests.post(url=pixela_end_point,json=user_param)
# print(responses.text)

graph_end_point=f"{pixela_end_point}/{username}/graphs"

graph_param={
    "id":graph_id,
    "name":"Programming",
    "unit":"Hours",
    "type":"float",
    "color":"sora"
    }

header={
    "X-USER-TOKEN":token
}

# responses=requests.post(url=graph_end_point,json=graph_param,headers=header)
# print(responses.text)

# today=datetime.now()
today=datetime(year=2022,month=5,day=19)
pixel_creation_end_point=f"{pixela_end_point}/{username}/graphs/{graph_id}"

pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"2"
}

# response=requests.post(url=pixel_creation_end_point,json=pixel_data,headers=header)
# print(response.text)

update_endpoint=f"{pixela_end_point}/{username}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"

new_pixel_data={
    "quantity":"1.45"
}

# response=requests.put(url=update_endpoint,json=new_pixel_data,headers=header)
# print(response.text)

delete_endpoint=f"{pixela_end_point}/{username}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
response=requests.delete(url=delete_endpoint,headers=header)
print(response.text)
