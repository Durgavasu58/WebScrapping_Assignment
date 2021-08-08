import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on"
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')

titles=soup.find_all('div',class_='_4rR01T')
ratings=soup.find_all('div',class_='_3LWZlK')
reviews=soup.find_all('span',class_='_2_R_DZ')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')

# store in list
mt=[]
mr=[]
mre=[]
mp=[]

for title,rating,review,price in zip(titles,ratings,reviews,prices):
	mt.append(title.text)
	mr.append(rating.text)
	mre.append(review.text)
	mp.append(price.text)
	
#saving data in csv

d={'mt':mt,'mr':mr,'mre':mre,'mp':mp}
model=pd.DataFrame(data=d)

model.to_csv('model.csv')