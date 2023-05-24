import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = '' #use .env file
TO = '' #use .env file
PASS = '' #use .env file

now = datetime.datetime.now()
email_content = ''

def extract_news(url):
    """ extracts stories from hacker news"""
    print(f'exteacting stories from Hacker News...')
    cnt = ''
    cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html-parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i+1)+'::'+tag.text+"\n"+'<br>') if tag.text!='More' else '')
        #print(tag.prettify) #find_all('span', attrs={'class':'sitestr'})
    return cnt

cnt = extract_news('https://news.ycombinator.com')
email_content += cnt
email_content += ('<br>------</br>')
email_content += ('<br><br>End of Message')

print(f'Composing email...')
msg = MIMEMultipart()
msg['Subject'] = f'{datetime.date.today()}: New stories from Hacker News'
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(email_content, 'html'))

print(f'Initialising server...')
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())
print(f'Email sent')
server.quit()