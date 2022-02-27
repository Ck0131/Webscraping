from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div", {"class":"_13oc-S"})
#length of the web page:
#print(len(containers))

#html of the web page:
#print(soup.prettify(containers[0]))

container = containers[0]

#single product name in the webpage extract:
#print(container.div.img["alt"])

# price and offer of product:
price = container.findAll("div", {"class":"col col-5-12 nlI3QM"})
#print(price[0].text)

#rating method:
ratings = container.findAll("div",{"class":"gUuXy-"})
#print(ratings[0].text)

#all product name,price and rating:
filename = "product.csv"
f = open(filename,"w")

headers = "product_name,pricing,rating\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    price_container = container.findAll("div", {"class":"col col-5-12 nlI3QM"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div",{"class":"gUuXy-"})
    rating = rating_container[0].text

    #print("product_name:"+product_name)
    #print("price:"+price)
    #print("rating:"+rating)

#split the price and offer in the product:

    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price = "Rs." +rm_rupee[1]
    split_price = add_rs_price.split('E')
    final_price = split_price[0]

    split_rating = rating.split(" ")
    final_rating = split_rating[0]

    print(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
    f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")

f.close()
