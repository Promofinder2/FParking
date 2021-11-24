import os
from pandas.core.frame import DataFrame
import pydantic
from selenium import webdriver
import model
import database
import importlib
import datetime
import time
import pandas as pd
import numpy as np
from typing import List,Optional
def get_TimeLine():
    start_date = '03/15/2021'
    start_date = datetime.datetime.strptime(start_date,'%m/%d/%Y')
    base = datetime.datetime.today()
    time_range =base - start_date
    numdays = int(time_range.days)
    date_list = [(base - datetime.timedelta(days=x)).strftime('%m/%d/%Y') for x in range(numdays)]
    return date_list
def get_date_query(web,date):

    web.get('https://www.flashreceipt.com')
    time.sleep(1)
    cardnum = '9411'
    ccnum = web.find_element_by_xpath('//*[@id="CreditCard"]')
    trans = web.find_element_by_xpath('//*[@id="DepartureDate"]')
    search = web.find_element_by_xpath('//*[@id="ReceiptSearchTable"]/tbody/tr[8]/td/button')
    variance =web.find_element_by_xpath('//*[@id="Variance"]/option[12]')
    visa = web.find_element_by_xpath('//*[@id="CreditCardType"]/option[11]')
    texas = web.find_element_by_xpath('//*[@id="State"]/option[43]')
    ccnum.send_keys(cardnum)
    visa.click()
    trans.send_keys(date)
    texas.click()
    variance.click()
    search.click()
    time.sleep(.5)
    return web

def get_FlashReceipts():
    flashReceipt_List = []
    timeline = get_TimeLine()
 
    web = webdriver.Chrome(executable_path='C:/Users/O/Desktop/chromedriver.exe')
    
    try:
        for count,date in enumerate(timeline):
            web = get_date_query(web,date)
            summary_table = web.find_elements_by_class_name('summary-table')
            for row in summary_table:
                name_list = row.find_elements_by_class_name('DataName') 
                location_list = row.find_elements_by_class_name('DataLocation')
                city_list = row.find_elements_by_class_name('DataCity')
                arrival_list = row.find_elements_by_class_name('DataArrival')
                departure_list = row.find_elements_by_class_name('DataDeparture')
                payment_list = row.find_elements_by_class_name('DataPayment')
                receipt_list = row.find_elements_by_class_name('DataReceipt')
                
                for name,location,city,arrival,departure,payment,receipt in zip (name_list,location_list,city_list,
                arrival_list,departure_list,payment_list,receipt_list):
                    table_attributes = {
                        'DataName':name.text,'DataLocation':location.text,
                        'DataCity':city.text,'DataArrival':arrival.text,'DataDeparture':departure.text,
                        'DataPayment':payment.text,'DataReceipt':receipt.text
                        }

                    rec = model.FlashReceipt(**table_attributes)

                    flashReceipt_List.append(rec)
                

        return flashReceipt_List
    except ValueError as e:
        
        print(f'VALUE ERROR | {e}')

    finally:
        print('FINALLY')
        return flashReceipt_List



def main ():
    df = pd.DataFrame()

    flashReceipt_List = get_FlashReceipts()
    FlashRec_List: List[model.FlashReceipt] = [f for f in flashReceipt_List]
    df = DataFrame([x.__dict__ for x in FlashRec_List])

    df.to_excel('FParkRepo.xlsx',index=False)
    print('Success!')

if __name__ == '__main__':
    main()