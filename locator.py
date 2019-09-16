import requests


url = input("Please enter a valid URL:")

response = requests.get(url)
print(response.text)
