from selenium import webdriver
from config import keys, credentials
from time import sleep

sizes = 0

def order(k,s,c):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(k['product_url'])

    driver.implicitly_wait(2)
    # click sign in button
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/header/div[1]/section/ul/li[1]/button').click()

    # Enter username
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/form/div[2]/input').send_keys(c["user"])
    # Enter password
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/form/div[3]/input').send_keys(c["pass"])
    # Click sign in
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/form/div[6]/input').click()

    sleep(1)
    # Get size 10
    attempts = 2
    result = False
    while(attempts<2):
        try:
            d2 = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/ul/li[9]/button').click()
            result = True
        except(StaleElementException):
            pass
        attempts +=1

    # Add to bag
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/div/button').click()
    # click check out
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/header/div[1]/section/ul/li[3]/a/i').click()
    sleep(1)

    # Click member checkout
    driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[2]/aside/div[6]/div/button[1]').click()
    sleep(1)
    # Terms and conditions
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div[1]/div[2]/div[2]/div/div[1]/label[1]').click()
    # Continue to billing
    driver.find_element_by_xpath('//*[@id="shippingSubmit"]').click()
    # Continue to payment
    driver.find_element_by_xpath('//*[@id="billingSubmit"]').click()


    # card name
    #driver.find_element_by_xpath('//*[@id="CreditCardHolder"]').send_keys(k["name"])
    # card number
    driver.find_element_by_xpath('//*[@id="KKnr"]').send_keys(k["card"])
    # card expiry month
    driver.find_element_by_xpath('//*[@id="KKMonth"]/option[{}]'.format(k['exp_month'])).click()
    # card expiry year
    driver.find_element_by_xpath('//*[@id="KKYear"]/option[{}]'.format(k['exp_year'])).click()
    # cvv
    #driver.find_element_by_xpath('//*[@id="CCCVC"]').send_keys(k["cvv"])

    # Place order
    #driver.find_element_by_xpath('//*[@id="BtnPurchase"]').click()



if __name__ == '__main__':
    order(keys,sizes,credentials)
