import requests
data=requests.get('https://chatgpt.com/')
file=open("webpage.html",'wb')
file.write(data.content)
file.close()