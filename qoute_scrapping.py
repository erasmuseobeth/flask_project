''' scrapping qoutes at http://qoutes.toscrape.com
import bs4
import requests


url = input('Input url to scrape qoutes from::')
page = 1
page_still_valid = true
while page_still_valid:
    url = url+str(page)
    res = requests.get('url')
    res.text
    if 'No qoutes found!' in res.text:
        break
    soup = bs4.BeautifulSoup('res.text','lxml')
    authors = set()
    for name in soup.select('.author'):
        authors.add(name.text)
    qoutes = []
    for qoutes in soup.select('.text')
        qoutes.append(qoute.text)

    for item in soup.select('.tag-item');
        print(item.text)
    page +=1
    

