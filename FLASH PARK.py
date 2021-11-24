import pandas as pd
import datetime
import numpy as np
import requests
from requests_toolbelt.utils import dump
from selenium.common.exceptions import NoSuchElementException
import os
import time
import regex as re
from selenium import webdriver
from collections import OrderedDict
def get_tdate_list(num = 270):
    numdays = num
    base = datetime.datetime.today()
    tdate_list = [(base - datetime.timedelta(days=x)).strftime('%m/%d/%Y') for x in range(numdays)]
    return tdate_list
os.chdir('C:/Users/O/Desktop')
#tdate = '08/31/2021'
table_str_keys_list=[]
table_str_vals_list=[]
web = webdriver.Chrome(executable_path='C:/Users/O/Desktop/chromedriver.exe')

for tdate in get_tdate_list():
    i=2
    time.sleep(2)
    hours2=web.find_element_by_xpath('//*[@id="Hour"]/option[01]')
    hours3=web.find_element_by_xpath('//*[@id="Hour"]/option[02]')
    hours4=web.find_element_by_xpath('//*[@id="Hour"]/option[03]')
    hours5=web.find_element_by_xpath('//*[@id="Hour"]/option[04]')
    hours6=web.find_element_by_xpath('//*[@id="Hour"]/option[05]')
    hours7=web.find_element_by_xpath('//*[@id="Hour"]/option[06]')
    hours8=web.find_element_by_xpath('//*[@id="Hour"]/option[07]')
    hours9=web.find_element_by_xpath('//*[@id="Hour"]/option[08]')
    hours10=web.find_element_by_xpath('//*[@id="Hour"]/option[09]')
    hours11=web.find_element_by_xpath('//*[@id="Hour"]/option[10]')
    hours12=web.find_element_by_xpath('//*[@id="Hour"]/option[11]')
    hours13=web.find_element_by_xpath('//*[@id="Hour"]/option[12]')
    hours14=web.find_element_by_xpath('//*[@id="Hour"]/option[13]')
    hours15=web.find_element_by_xpath('//*[@id="Hour"]/option[14]')
    hours16=web.find_element_by_xpath('//*[@id="Hour"]/option[15]')
    hours17=web.find_element_by_xpath('//*[@id="Hour"]/option[16]')
    hours18=web.find_element_by_xpath('//*[@id="Hour"]/option[17]')
    hours19=web.find_element_by_xpath('//*[@id="Hour"]/option[18]')
    hours20=web.find_element_by_xpath('//*[@id="Hour"]/option[19]')
    hours21=web.find_element_by_xpath('//*[@id="Hour"]/option[20]')
    hours22=web.find_element_by_xpath('//*[@id="Hour"]/option[21]')
    hours23=web.find_element_by_xpath('//*[@id="Hour"]/option[22]')
    hours24=web.find_element_by_xpath('//*[@id="Hour"]/option[23]')
    hours_dict = OrderedDict([
        (2,hours2),
        (3,hours3),
        (4,hours4),
        (5,hours5),
        (6,hours6),
        (7,hours7),
        (8,hours8),
        (9,hours9),
        (10,hours10),
        (11,hours11),
        (12,hours12),
        (13,hours13),
        (14,hours14),
        (15,hours15),
        (16,hours16),
        (17,hours17),
        (18,hours18),
        (19,hours19),
        (20,hours20),
        (21,hours21),
        (22,hours22),
        (23,hours23),
        (24,hours24)
        ])
    for hour in hours_dict.keys():  
        try:
            web.get('https://www.flashreceipt.com')
            time.sleep(2)
            hours2=web.find_element_by_xpath('//*[@id="Hour"]/option[01]')
            hours3=web.find_element_by_xpath('//*[@id="Hour"]/option[02]')
            hours4=web.find_element_by_xpath('//*[@id="Hour"]/option[03]')
            hours5=web.find_element_by_xpath('//*[@id="Hour"]/option[04]')
            hours6=web.find_element_by_xpath('//*[@id="Hour"]/option[05]')
            hours7=web.find_element_by_xpath('//*[@id="Hour"]/option[06]')
            hours8=web.find_element_by_xpath('//*[@id="Hour"]/option[07]')
            hours9=web.find_element_by_xpath('//*[@id="Hour"]/option[08]')
            hours10=web.find_element_by_xpath('//*[@id="Hour"]/option[09]')
            hours11=web.find_element_by_xpath('//*[@id="Hour"]/option[10]')
            hours12=web.find_element_by_xpath('//*[@id="Hour"]/option[11]')
            hours13=web.find_element_by_xpath('//*[@id="Hour"]/option[12]')
            hours14=web.find_element_by_xpath('//*[@id="Hour"]/option[13]')
            hours15=web.find_element_by_xpath('//*[@id="Hour"]/option[14]')
            hours16=web.find_element_by_xpath('//*[@id="Hour"]/option[15]')
            hours17=web.find_element_by_xpath('//*[@id="Hour"]/option[16]')
            hours18=web.find_element_by_xpath('//*[@id="Hour"]/option[17]')
            hours19=web.find_element_by_xpath('//*[@id="Hour"]/option[18]')
            hours20=web.find_element_by_xpath('//*[@id="Hour"]/option[19]')
            hours21=web.find_element_by_xpath('//*[@id="Hour"]/option[20]')
            hours22=web.find_element_by_xpath('//*[@id="Hour"]/option[21]')
            hours23=web.find_element_by_xpath('//*[@id="Hour"]/option[22]')
            hours24=web.find_element_by_xpath('//*[@id="Hour"]/option[23]')
            hours_dict = OrderedDict([
                (2,hours2),
                (3,hours3),
                (4,hours4),
                (5,hours5),
                (6,hours6),
                (7,hours7),
                (8,hours8),
                (9,hours9),
                (10,hours10),
                (11,hours11),
                (12,hours12),
                (13,hours13),
                (14,hours14),
                (15,hours15),
                (16,hours16),
                (17,hours17),
                (18,hours18),
                (19,hours19),
                (20,hours20),
                (21,hours21),
                (22,hours22),
                (23,hours23),
                (24,hours24)
                ])
            cardnum = '9411'
            ccnum = web.find_element_by_xpath('//*[@id="CreditCard"]')
            trans = web.find_element_by_xpath('//*[@id="DepartureDate"]')
            search = web.find_element_by_xpath('//*[@id="ReceiptSearchTable"]/tbody/tr[8]/td/button')
            variance =web.find_element_by_xpath('//*[@id="Variance"]/option[10]')
            visa = web.find_element_by_xpath('//*[@id="CreditCardType"]/option[9]')
            texas = web.find_element_by_xpath('//*[@id="State"]/option[43]')
            ccnum.send_keys(cardnum)
            visa.click()
            trans.send_keys(tdate)
            texas.click()
            variance.click()
            hours_dict[i].click()
            search.click()
            
            summary_table = web.find_elements_by_class_name('summary-table')
            dir(summary_table)

            summary_table.__str__()
            dir(summary_table[0])
            row = summary_table[0]
            row.find_elements_by_class_name('DataName')
            x = row.find_elements_by_class_name('DataName')
            x[2].text
            len(summary_table)
            for each in summary_table:
                things = each.text.split('\n')
                if len(things) == 1:
                    print('0 found')
                elif len(things) == 2:
                    print('1 found')
                elif len(things) == 3:
                    print('2 found')
                elif len(things) == 4:
                    print('3 found')
                elif len(things) >=5:
                    print(len(things)-1,' found')
                    headers = things[0].split(' ')
                    for thing in things:
                        if 'CARSON' in thing:
                            web.find_element_by_xpath('//*[@id="FlashForm"]/div[3]/table[2]/tbody/tr[1]/td[7]/button').click()
                            receipt = web.find_element_by_xpath('//*[@id="FlashForm"]/div[3]/table[2]/tbody/tr[1]/td[7]/button')
                            time.sleep(1)
                            receipt.click()
                            table = web.find_elements_by_xpath('//*[@id="FlashForm"]/div/div/div[1]/div[3]/table')
                            table_str_keys = []
                            table_str_vals = []
                            print('made to table')
                            for h in table:
                                tmp_str=h.text.split('\n')
                                for st in tmp_str:
                                    if ':' in st:
                                        table_str_keys.append(st.split(':',1)[0])
                                        table_str_vals.append(st.split(':',1)[1::])
                            table_str_keys_list.append(table_str_keys)
                            table_str_vals_list.append(table_str_vals)
                        
                            web.find_element_by_xpath('//*[@id="EmailButton"]').click()
                            email = web.find_element_by_xpath('//*[@id="RecipientEmailAddress"]')
                            #email.send_keys('ocarson@awtxlaw.com')
                            email.send_keys('yadayada@gmail.com')
                            web.find_element_by_xpath('//*[@id="EmailSendForm"]/button[2]').click()
                            time.sleep(1)
                            back_to_summary_list = web.find_element_by_xpath('//*[@id="FlashForm"]/div/div/div[1]/div[1]/div[1]/div[1]/button')
                            back_to_summary_list.click()
                            time.sleep(1)
                            web.find_element_by_xpath('//*[@id="FlashForm"]/div[3]/table[2]/tbody/tr[2]/td[7]/button').click()                       
                            receipt = web.find_element_by_xpath('//*[@id="FlashForm"]/div[3]/table[2]/tbody/tr[1]/td[7]/button')
                            time.sleep(1)
                            receipt.click()
                            table = web.find_elements_by_xpath('//*[@id="FlashForm"]/div/div/div[1]/div[3]/table')
                            table_str_keys = []
                            table_str_vals = []
                            print('made to table')
                            for h in table:
                                tmp_str=h.text.split('\n')
                                for st in tmp_str:
                                    if ':' in st:
                                        table_str_keys.append(st.split(':',1)[0])
                                        table_str_vals.append(st.split(':',1)[1::])
                            table_str_keys_list.append(table_str_keys)
                            table_str_vals_list.append(table_str_vals)

                        
                            web.find_element_by_xpath('//*[@id="EmailButton"]').click()
                            email = web.find_element_by_xpath('//*[@id="RecipientEmailAddress"]')
                            email.send_keys('yadayada@gmail.com')
                            web.find_element_by_xpath('//*[@id="EmailSendForm"]/button[2]').click()
                            time.sleep(1)
                            back_to_summary_list = web.find_element_by_xpath('//*[@id="FlashForm"]/div/div/div[1]/div[1]/div[1]/div[1]/button')
                            back_to_summary_list.click()                        
                            i+=1
        except NoSuchElementException:
            print(f'NO BILL: {tdate} | {hour}')
            i+=1
print(len(table_str_vals_list))
print(len(table_str_keys_list))
print(table_str_vals_list)
print(table_str_keys_list)
#r = requests.get('https://www.flashreceipt.com/')
#response = requests.post('https://www.flashreceipt.com/', data={'key1':'value1'})
#print(response.request.url)
#print(response.request.body)
#print(response.request.headers)
#resp = requests.get('https://www.flashreceipt.com/',)
#data = dump.dump_all(resp)
#print(data.decode('utf-8'))
#os.getcwd()
#os.chdir('..')
df = pd.DataFrame()
df['keys'] = table_str_keys_list
df['vals'] = table_str_vals_list
df.to_excel('test.xlsx',index=False)
