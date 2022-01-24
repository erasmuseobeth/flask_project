import requests
import bs4


url = input('Input url link to request >>\n')

tag_name = input('Enter HTML tag element of url link you want to grab >>\n\tp for paragraph\n\ttitle for title\n\tbody for body\n\tdiv for division element...e.t.c\n\t>>>')

result = requests.get(url)

result.text

soup = bs4.BeautifulSoup(result.text,'lxml')

print(soup)

soup.select('tag_name')[0].getText()
