import requests

def test_get_products():
   r = requests.get("http://localhost:8000/products")
   response = r.json()
   print (response)

test_get_products()
