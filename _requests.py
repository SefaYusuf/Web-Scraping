import requests
import json
# print(products['products'])
# user = "{'username': 'ömer', 'age': 27, 'email': 'omer@gmail.com'}"
# print(user['username'])
url = "https://dummyjson.com/products"
response = requests.get(url, params={'limit': 15, 'skip': 20})
print(response.status_code)
products = response.text
print(type(products))
products = json.loads(response.text)
print(type(products))
# products = products['products']
# for product in products:
#     print(product['title'])
print(products)