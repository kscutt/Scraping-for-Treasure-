import smtplib
import json
from bs4 import BeautifulSoup
import requests
import time
def get_page_html(url):
    page = requests.get(url)
    print(page.status_code)
    return page.content


# def get_ld_json(url: str) -> dict:
#     parser = "html.parser"
#     req = requests.get(url)
#     soup = BeautifulSoup(req.text, parser)
#     return json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))

#TODO: I think I am checking the wrong tags so it's always coming up as unavailable. Email is working tho 😇
def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("div", {"class": "product-inventory"})
    no_longer_avail = soup.findAll("div", {"class": "c-pwa-product-oos-rec-tray__lead-message"})

    if len(no_longer_avail) < 1:
        print("No Longer Available 🥲")
        return False

    elif len(out_of_stock_divs) < 1:
        print("item is available")
        return True
    # if len(out_of_stock_divs) < 1:
    #     print("item is available")
    #     return True
    else:
        return False

def check_inventory():
    #url = "https://www.urbanoutfitters.com/shop/uo-community-cares-paints-david-zembrano-we-rise-tee?category=mens-tops" #This one is out of stock
    url = "https://www.urbanoutfitters.com/shop/halo-classic-tee?category=SEARCHRESULTS&color=044&searchparams=q%3Dhalo&type=REGULAR&quantity=1&size=L"
    # page_json = get_ld_json(url)
    # print(page_json)
    page_html = get_page_html(url)
    while True:
        if check_item_in_stock(page_html) == True:
            #send_mail()
            print("Item is in stock")
        else:
            print("Item is out of stock")
            break


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('submarinecello@gmail.com', 'snhixaesdmadyzea')
    subject = "The cool shirt is back in stock 😎"
    body = 'Check the link! https://www.urbanoutfitters.com/shop/halo-classic-tee?category=SEARCHRESULTS&color=044&searchparams=q%3Dhalo&type=REGULAR&quantity=1&size=S'
    msg = "Subject: subject \n\nbody"
    server.sendmail('submarinecello@gmail.com','submarinecello@gmail.com',msg)
    print('Email has been sent')

    server.quit()

check_inventory()
