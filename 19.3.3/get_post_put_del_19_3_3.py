import requests
import json
import os

from requests_toolbelt.multipart.encoder import MultipartEncoder

# ________________01_post_new_pet________________
url = 'https://petstore.swagger.io/v2/pet'
headers = {'accept': 'application/json', 'content-type': 'application/json'}
data = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "Sebastian",
    "photoUrls": [
        "string"
    ],
    "tags": [{
        "id": 0,
        "name": "string"
    }],
    "status": "available"
}

res = requests.post(url,
                    headers=headers,
                    data=json.dumps(data,
                                    ensure_ascii=False).encode('utf-8'))

# if 'application/json' in res.headers['Content-Type']:
#     res.json()
# else:
#     res.text

petId = res.json()['id']

print(res.status_code)
print(res.text)

# ________________02_import_image_data________________

class DaTa:
    file_name = 'cat1.jpg'
    pet_photo = os.path.join(os.path.dirname(__file__), f'images/{file_name}')
    image_f = MultipartEncoder(fields=
                               {'file': (file_name, open(pet_photo, 'rb'), 'image/jpeg')})


# image_f = {'file': open('images/cat1.jpg', 'rb')} - outputs 415.
res = requests.post(url + f'/{petId}/uploadImage',
                    headers={'accept': 'application/json', 'Content-Type': DaTa.image_f.content_type},
                    data=DaTa.image_f)
print(res.status_code)
print(res.text)

# ________________03_update_the_pet________________
data = {
    "id": petId,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "Sebastian Jr.",
    "photoUrls": [
        "string"
    ],
    "tags": [{
        "id": 0,
        "name": "string"
    }],
    "status": "available"
}

res = requests.put(url,
                   headers=headers,
                   data=json.dumps(data,
                                   ensure_ascii=False).encode('utf-8'))

print(res.status_code)
print(res.text)

# ________________04_find_by_status________________

res = requests.get(url + f'/findByStatus',
                   params={'status': 'available'},
                   headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)

# ________________05_find_pet_by_id________________

res = requests.get(url=f"https://petstore.swagger.io/v2/pet/{petId}",
                   params={'status': 'available'},
                   headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)

# ________________06_post_pet_in_store________________

res = requests.post(url=f"https://petstore.swagger.io/v2/pet/{petId}",
                    params={'petId': f'{petId}', 'name': 'Sebastian', 'status': 'available'},
                    headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)

# ________________07_delete_pet_by_id________________

res = requests.delete(url=f"https://petstore.swagger.io/v2/pet/{petId}",
                      params={'petId': f'{petId}', 'name': 'Sebastian', 'status': 'available'},
                      headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)

# ________________08_post_pet_order_________________

url = 'https://petstore.swagger.io/v2/pet'
headers = {'accept': 'application/json', 'content-type': 'application/json'}

data = {
  "id": 0,
  "petId": petId,
  "quantity": 0,
  "shipDate": "2022-11-17T14:14:25.245Z",
  "status": "placed",
  "complete": True
}

res = requests.post(url='https://petstore.swagger.io/v2/store/order',
                    headers=headers,
                    data=json.dumps(data,
                                    ensure_ascii=False).encode('utf-8'))

order_id = res.json()['id']

print(res.status_code)
print(res.text)

# ________________09_find_pet_order_________________

res = requests.get(url=f'https://petstore.swagger.io/v2/store/order/{order_id}',
                   params={'status': 'available'},
                   headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)

# ________________10_delete_pet_order_________________

res = requests.delete(url=f'https://petstore.swagger.io/v2/store/order/{order_id}',
                      params={'status': 'available'},
                      headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)

# ________________11_delete_pet_order_________________

res = requests.get(url=f'https://petstore.swagger.io/v2/store/inventory',
                   headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)

# ________________12_user_create_array_________________

url = 'https://petstore.swagger.io/v2/user/'
headers = {'accept': 'application/json', 'content-type': 'application/json'}

data = [
    {
        "id": 0,
        "username": "peter001",
        "firstName": "Peter",
        "lastName": "Johnson",
        "email": "string",
        "password": "qaz123",
        "phone": "string",
        "userStatus": 0
    }
]

username_a = data[0]["username"]

res = requests.post(url='https://petstore.swagger.io/v2/user/createWithArray',
                    headers=headers,
                    data=json.dumps(data,
                                    ensure_ascii=False).encode('utf-8'))

print(res.status_code)
print(res.text)

# ________________13_user_create_list_________________

data = [
    {
        "id": 0,
        "username": "john002",
        "firstName": "John",
        "lastName": "Peterson",
        "email": "string",
        "password": "123qaz",
        "phone": "string",
        "userStatus": 0
    }
]

username_b = data[0]["username"]
password_b = data[0]["password"]

res = requests.post(url='https://petstore.swagger.io/v2/user/createWithList',
                    headers=headers,
                    data=json.dumps(data,
                                    ensure_ascii=False).encode('utf-8'))

print(res.status_code)
print(res.text)

# ________________14_get_user_by_name_________________

res = requests.get(url=f'https://petstore.swagger.io/v2/user/{username_a}',
                   headers={'accept': 'application/json'})

user_id = res.json()['id']

print(res.status_code)
print(res.text)

# ________________15_update_user__________________

data = {
  "id": user_id,
  "username": "jackson100",
  "firstName": "Samuel",
  "lastName": "Jackson",
  "email": "string",
  "password": "qaz321",
  "phone": "string",
  "userStatus": 0
}

username_a = data["username"]

res = requests.put(url=f'https://petstore.swagger.io/v2/user/{username_a}',
                   headers=headers,
                   data=json.dumps(data,
                                   ensure_ascii=False).encode('utf-8'))

print(res.status_code)
print(res.text)

# ________________16_delete_user__________________

res = requests.delete(url=f"https://petstore.swagger.io/v2/user/{username_a}",
                      headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)

# ________________17_user_login__________________

res = requests.get(url=f'https://petstore.swagger.io/v2/user/login?username={username_b}&password={password_b}',
                   headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)

# ________________18_user_logout__________________

res = requests.get(url='https://petstore.swagger.io/v2/user/logout',
                   headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)

# ________________19_user_create__________________

data = {
  "id": 0,
  "username": "thompson003",
  "firstName": "Doctor",
  "lastName": "Thompson",
  "email": "string",
  "password": "321zaq",
  "phone": "string",
  "userStatus": 0
}

username_b = data["username"]

res = requests.post(url='https://petstore.swagger.io/v2/user',
                    headers=headers,
                    data=json.dumps(data,
                                    ensure_ascii=False).encode('utf-8'))

print(res.status_code)
print(res.text)