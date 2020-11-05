import requests
from bs4 import BeautifulSoup as bs

html = requests.get("https://stepik.org/media/attachments/lesson/209723/5.html").content
soup = bs(html, 'html.parser')
sum = 0
for x in soup.find_all("td"):
    sum += int(x.text.strip())

print(sum)