from bs4 import BeautifulSoup
from twilio.rest import Client 
import requests
import csv

source = requests.get('https://www.cricbuzz.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('scores.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Match Name', 'Score', 'Summary'])

body = "";

for table in soup.findAll('div', attrs = {'class':'cb-col cb-col-25 cb-mtch-blk'}):
    match = table.a['title']

    print('Match Name : ' + match)
    body += match
    
    
    score = table.div.text
    body += score

    print('score :' + score)
    try:
        summary = table.find('div', attrs={'class': 'cb-ovr-flo cb-text-live'}).text
        print('Summary : ' + summary);
        body += summary
    except Exception as e:
        summary = ""
    


    csv_writer.writerow([match, score, summary])

csv_file.close()

account_sid = 'AC771cc8f81cea7a43c1cfc19e60f68f3f' 
auth_token = <YOUR AUTH TOKEN>
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12055836887',   
                              body=  body ,
                              to= <YOUR TWILIO REGISTERED MOBILE NUMBER>
                          ) 

print(message.sid)