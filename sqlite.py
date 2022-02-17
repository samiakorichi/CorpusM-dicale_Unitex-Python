import sqlite3
#pip install beautifulsoup4
from bs4 import BeautifulSoup
from lxml import html
import sys
import requests
con = sqlite3.connect('extraction.db')
cur = con.cursor()

requete='''CREATE TABLE IF NOT EXISTS EXTRACTION (ID PRIMARY KEY,POSOLOGIE TEXT)'''
cur.execute(requete)
con.commit()
data=open('corpus-medical_snt/concord.html', 'r')
soup=BeautifulSoup(data,'lxml')
lesa=soup.find_all("a")
Id=1
for a in lesa:
	requete="INSERT INTO EXTRACTION (ID,POSOLOGIE ) VALUES( "+str(Id)+",\""+str(a.text)+"\")"
	Id+=1
	cur.execute(requete)
	con.commit()
con.close()	
