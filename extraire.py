#pip install beautifulsoup4
from bs4 import BeautifulSoup
from lxml import html
import sys
import requests
from string import ascii_uppercase
import os
interval=sys.argv[1]
port=sys.argv[2]
interval=sys.argv[1]
alfa=list(interval)
listSubstance=[]
nombreParLettre=[]
with open('subst.dic', 'w',encoding="utf_16_le") as objf:
	for x in range(ord(alfa[0])-65,ord(alfa[2])-64):
		url='http://127.0.0.1:'+port+'/vidal/vidal-Sommaires-Substances-'+ascii_uppercase[x]+'.htm'
		Alphabet=ascii_uppercase[x]
		data=requests.get(url).text
		soup=BeautifulSoup(data,'lxml')
		alphabet="letter"+Alphabet.lower()
		ul=soup.find("ul", {"id": alphabet})
		listLien=ul.find_all("a")
		file=open('infos1.txt','a')
		nbr=0
		for a in listLien:
			nbr=nbr+1
			NomSubstance=a.text
			decoderNomSubstance=NomSubstance.encode("iso-8859-1").decode("utf-8")+",.N+subst"
			decoderNomSubstance=decoderNomSubstance+'\n'
			objf.write(decoderNomSubstance)
			listSubstance.append(decoderNomSubstance)
		info="Total de "+str(ascii_uppercase[x])+" : "+str(nbr)+"\n"
		file.write(info)
		file.close()
file=open('infos1.txt','a')
file.write("Nombre total des substances actives : 		"+str(len(listSubstance)))
file.close()
