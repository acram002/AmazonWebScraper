# import libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib


# Connect to website and pull in data

URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
title = soup2.find(id='productTitle').get_text()
#price = soup2.find(id='corePriceDisplay_desktop_feature_div').get_text()
print(title)
#print(price)

# Clean up the data

#price = price.strip()[1:]
title = title.strip()
print(title)

# Create a Timestamp for output to track when data was collected
import datetime
today = datetime.date.today()
print(today)

# Create CSV and write headers and data into the file
import csv
header = ['Title', 'Date']
data = [title, today]

with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data) 

import pandas as pd
df = pd.read_csv(r'/Users/alexcramer/AmazonWebScraperDataset.csv')
print(df)

# Appending data to csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

    #Combine all of the above code into one function

def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    #price = soup2.find(id='priceblock_ourprice').get_text()

    #price = price.strip()[1:]
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Date']
    data = [title, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    if(price < 14):
        send_mail()

# Runs check price after set time 

while(True):
    check_price()
    time.sleep(86400)
    
    
import pandas as pd
df = pd.read_csv(r'/Users/alexcramer/AmazonWebScraperDataset.csv')
print(df)
    
# Sends email

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('crameralex6@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "Subject"
    body = "Message"
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'crameralex6@gmail.com',
        msg
     
    )