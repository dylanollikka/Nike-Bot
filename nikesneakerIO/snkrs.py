from selenium import webdriver
from splinter import Browser
import requests
import bs4
import time

product_url = 'https://www.supremenewyork.com/'
shop_ext = 'shop/all/'
checkout_ext = 'checkout/'
name = 'name'

info = {
"category": "tops_sweaters",
"product": "Dyed Basketball Jersey",
"color": "Black"
}
#b = Browser()
driver = webdriver.Chrome('./chromedriver')

r = requests.get('{}{}{}'.format(product_url, shop_ext, info['category'])).text
soup = bs4.BeautifulSoup(r,'lxml')
temp_tuple = []
temp_link = []

for link in soup.find_all("a",href=True):
    temp_tuple.append((link["href"], link.text))

for i in temp_tuple:
    if i[1] == info["product"] or i[1]==info["color"]:
        temp_link.append(i[0])
final_link = list(set([x for x in temp_link if temp_link.count(x)==2]))[0]

def visit_link():
    final_link2 = product_url + final_link
    print(final_link2)
    driver.get(final_link2)

def add_to_cart():
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    # click check out
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

def billing():
    # name
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(name)
    # email
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(name)
    # phone
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(name)
    #address
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys('10312 111 ST NW')
    #house no.
    driver.find_element_by_xpath('//*[@id="oba3"]').send_keys('123')
    # zip
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys('t3t2t1')
    #City
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys('Edmonton')
    # state
    driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[1]').click()
    # country
    driver.find_element_by_xpath('//*[@id="order_billing_country"]/option[2]').click()
    # card type
    driver.find_element_by_xpath('//*[@id="credit_card_type"]').click()
    # number
    driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys('123456789101234')
    # month
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[2]').click()
    # year
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[4]').click()
    # CVV
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys('123')
    # terms and cond.
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()
    # pay
    #driver.find_element_by_xpath('//*[@id="pay"]/input').click()

visit_link()
add_to_cart()
billing()
