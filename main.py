import requests
from bs4 import BeautifulSoup as bs

user_name = input('Input Github Name: ')
url = 'https://github.com/' + user_name
r = requests.get(url)
soup = bs(r.content, 'html.parser')
photo = soup.find('img', {'class':'avatar avatar-user width-full border color-bg-default'})['src']

print(photo)
