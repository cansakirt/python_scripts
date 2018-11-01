''' This script scrapes ~130 pages of Last Call items on Decathlon website.
    Export them to CSV as "price|item_name|item_link|image_link".

    As of 25-OCT-2018, there are 15 items per page and 133 pages in total.
    It takes ~15 minutes. So, something definitely should be improved.
    May be faster if CSV was appended page by page instead of line by line.

    Usage:
        % python decathlon_scrape.py

    Can Sakirt - October 2018
'''

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


def opengetpage(link):
    ''' Open link. Return list of items (products).
        '''
    # Open link
    html = urlopen(link)
    # Convert to a bs object
    bsObj = BeautifulSoup(html, "lxml")
    # Find all <div> elements with the id=bc-sf-filter-products,
    # this returns a list, so select the zeroth one (notice [0] at the end)
    table = bsObj.findAll("div", {"id": "bc-sf-filter-products"})[0]
    # Find all <div> elements with the class=grid__item large--one-third... etc
    # Returns a list of 15 items. (Decathlon displays 15 items on this page.)
    items = table.findAll("div", {"class": "grid__item large--one-third \
                          one-half collectionProduct \
                          js-bln-product"})
    return items


def get_items(item):
    ''' Parse each item. These are div elements for each product.  '''
    # Get img element's data-src and make it a proper link
    image_link = "https:" + item.img["data-src"]
    # Get the text in a that is under p
    item_name = item.p.a.get_text()
    # Get a element's href and make it a proper link
    item_link = "https://www.decathlon.com" + item.p.a["href"]
    # Get text (price) of the first element with said attributes
    price = item.findAll(attrs={"class": "productPrice collectionProduct-price\
                         u-marginBottom0x"})[0].get_text()
    # Strip price of spaces and other text.
    price = only_price(price)
    # Turn this data into a list
    current_item = [price, item_name, item_link, image_link]
    # return the current_item i.e. product info for 1.
    return current_item


def only_price(t):
    ''' Strips the prices got from Decathlon's products.
        Strips different kinds of prices.
        See HTML code where the prices are.'''
    t = t.strip()
    if "\n" in t:
        return t.replace("        ", "").split("\n")[1]
    elif " " in t:
        return t.replace("        ", "").split(" ")[1]
    else:
        return t


def write_to_file(line):
    ''' Writes each line into csv. Default location is C:
        It may require run as admin.'''
    print(line)  # printing for testing. Delete this & return to write to file
    return       # delet dis
    with open(r"C:\decathlon_last_call.csv", "a", newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow(line)


def number_of_pages():
    ''' Looks at the last-call page and finds the last page
        by looking at the paginator on the bottom of the page.'''
    decathlon_page = "https://www.decathlon.com/collections/last-call"
    html1 = urlopen(decathlon_page)
    bsObj1 = BeautifulSoup(html1, "lxml")
    number = bsObj1.select('[id="bc-sf-filter-products"]')[0] \
                   .select('[class="paginate-bottom"]')[0] \
                   .findAll('span')[4].get_text()
    number = int(number)  # convert to int because it was string.
    return number


# Number of pages
number = 3  # use this if you wanna test a couple of pages.
number = number_of_pages()

for i in range(1, number):
    # iterate over pages and return 15 items.
    decathlon_page = "https://www.decathlon.com/collections/last-call?page="
    print("printing page no", i)
    # increment page in the url--ready to get the new page.
    decathlon_page += str(i)
    # get items of the current page.
    items = opengetpage(decathlon_page)
    for item in items:
        # iterate over each item of 15 that comes from one page.
        write_to_file(get_items(item))

# each line looks like this: [price, name, link, image link]
# ['$3.99', "Women's Hiking Short-Sleeve T-Shirt Techfresh 50", 'https://www.decathlon.com/collections/last-call/products/womens-short-sleeved-hiking-t-shirt-techfresh-50', 'https://cdn.shopify.com/s/files/1/1330/6287/products/13dc432b6d3b42f893727ca49408c140_large.jpg?v=1505958167']

# Links look like this:
# https://cdn.shopify.com/s/files/1/1330/6287/products/13dc432b6d3b42f893727ca49408c140_large.jpg?v=1505958167
# https://www.decathlon.com/collections/last-call/products/womens-short-sleeved-hiking-t-shirt-techfresh-50
