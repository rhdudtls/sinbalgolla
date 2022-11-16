import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests
from bs4 import BeautifulSoup


cred = credentials.Certificate('newdb.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://newbal-7f9a5-default-rtdb.firebaseio.com/'  
})

fs = open('women_url.txt', 'r')
url = fs.read().split("\n")
fs.close()
shoema = {}
shoeinfo = []
data2 = []
for i in url:
    temp1 = i.split("?")
    if temp1[0] == '':
        continue
    temp2 = temp1[1].split("=")[1]
    data2.append(temp2)

for i in data2:
    try:
        data = requests.get("https://www.nbkorea.com/product/productDetail.action?styleCode=" + i)

        soup = BeautifulSoup(data.text, 'html.parser')

        shoes_title = soup.select_one("#dispPrice").get_text()

        print(shoes_title)

    except:
        print("Exception")
        continue
    shoema[i] = shoes_title
    shoeinfo.append(shoema)

for i in shoeinfo:
    ref = db.reference('신발/가격')
    ref.update(i)
