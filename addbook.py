import requests

url = "http://127.0.0.1:8000/books"
data = {
    "id": 2,
    "title": "G F",
    "author": "Nuhin"
}

response = requests.post(url, json=data)
print(response.status_code)  # Should print 200
print(response.json())       # Should print the added book
