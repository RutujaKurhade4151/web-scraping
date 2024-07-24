from bs4 import BeautifulSoup
import requests
url=input("url :  ")
response=requests.get(url)
soup=BeautifulSoup(response.text, \
         "html.parser")
print(soup)
page_text=soup.get_text()
links=[a['href'] for a in soup.find_all('a',href=True)]
images=[img['src'] for img in soup.find_all('img',src=True)]
print("page text")
print(page_text)
print("links")
for link in links:
    print(link)

print("images")
for img in images:
    print(img)
































#else:
    #print("failed to retrive the web page :{response.status.code}")
