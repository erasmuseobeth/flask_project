# goal : go through each page of www.toscrape.com loop through all the pages and donload all the image and product disciption
import requests
import bs4



base_url = 'https://books.toscrape.com/catalogue/page{}.html'

page_num = 

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
products = soup.select('.product_pod')
example =   products['.image_container']['src']
 images = []
 for n in range(1,51)
     scrape_url = base_url.format(n)
     res = requests.get(scrape_url)

     soup = bs4.BeautifulSoup('res.text','lxml')
     books = soup.select('.product_pod')
     for books in books:
         #call image grabber
         image = 
         # call product desciption grabber
         description =
         # call post title
         title = 
         image_post = {'img':title,image,description}
         images .append(image_post)
