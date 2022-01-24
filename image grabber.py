''' grabbing images from a website by cyber330d'''
import requests
import bs4

url = input('enter website link to scrape images from ::')

# requests the given url from the internet servers.
img_resp =requests.get(url)

#parses the requested page in beautifulSoup library using lxml parser engine.
soup = bs4.BeautifulSoup(img_resp,'lxml')

#selects all HTML elements of tag img
img_link = soup.select(img)
#grabs all the image links source url value from the img_link dictionary of tags
img_link = ['src']

#loops through the image url requesting them 
for i in img_link:
    #requests the image link
    img_con= requests.get('https:'+src')
    #slices the image name and file format to be used for writing it when downloaded
    image_name = img_con[/: -1]
    #opens a file in write binary formatin this location
    f = open('/home/cyber330d/Downloads/webscrap img download/'+image_name','wb')
    #writes the binary content of the image to the file
    f.write(img_con.content)
    #closes the file
    f.close()

#code to display image in gridlock of 4 rows by 5 colums in maximised window
