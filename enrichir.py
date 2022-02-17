import re, sys, urllib.request
from string import ascii_uppercase
#opening files
corpus = open(sys.argv[1], 'r',encoding='utf-8')

trace = open('subst_corpus.dic', 'w+', encoding='utf_16_le')
info3=	open('info3.txt','a')
l=set()

cpt=0     #nb des substances trouvés dans corpus-medical.txt
lines = corpus.readlines()
for line in lines:
    substance = re.search(r'^[-*]?\s?(\w+)\s:?\s?(\d+|,|\d+.\d+|\d+.\d+.\d)+\s(mg|ml|µg|mcg|g|cp|amp|flacon).+', line, re.VERBOSE | re.I)     
    if substance:        # si une substance est trouvée 
        if substance.group(1).lower() != 'intraveineuse' and substance.group(1).lower() != 'eau' and substance.group(1).lower() != 'puis': #enlever les mots pris par erreur dans la regex
            trace.write(substance.group(1).lower()+',.N+subst\n')
            #dct.write(substance.group(1).lower()+',.N+subst\n')      # ecrire la substance dans les 2 dictionnaires
            cpt+=1
            print(str(cpt)+" : "+substance.group(1))
            l.add(str(substance.group(1)).lower())
subst = open('subst.dic', 'r', encoding='utf_16_le')
lines = subst.readlines()
l=sorted(l)
cptl=0
cptk=0
Total=0
for substance in l:
	Total+=1
	lettre=ord(substance.upper()[0])-65
	if lettre!=cptl:
		info="----------------------------------------------------\nTotal de "+str(ascii_uppercase[cptl])+" : "+str(cptk)+"\n----------------------------------------------------\n"
		info3.write(info)
		cptl=lettre
		cptk=1
	info3.write(substance+",.N+subst\n")
	cptk+=1
info="----------------------------------------------------\nNombre total des substances actives : "+str(Total)+"\n----------------------------------------------------\n"	
info3.write(info)
info3.close()		
l=set(l)
for line in lines:
	substance=line.split(',')[0]
	l.add(substance)
l=sorted(l)	
cpt=[0]*26
with open('subst.dic', 'w',encoding="utf_16_le") as objf:	
	for substance in l:
		lettre=ord(substance.upper()[0])-65
		if lettre>=0 and lettre<=25:
			objf.write(substance+",.N+subst\n")
			cpt[lettre]=cpt[lettre]+1
	objf.close()		
			
Total=0		
with open('info2.txt', 'w+', encoding='utf-8') as info2:
	for x in range(0,26):
		Total+=cpt[x]
		info="Total de "+str(ascii_uppercase[x])+" : "+str(cpt[x])+"\n"
		info2.write(info)
	info="----------------------------------------------------\nNombre total des substances actives : "+str(Total)+"\n----------------------------------------------------\n"	
	info2.write(info)
	info2.close()
subst.close()


