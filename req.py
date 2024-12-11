import requests
data=requests.get('https://www.google.com')
print(data)# that code give only responce code
# print(data.text)
print(data.content)# that code give a content all about file