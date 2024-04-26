# Text analysis using Natural Language processing NLTK libraries

import re
import nltk
import string
import textstat
import requests
from bs4 import BeautifulSoup

#--------------Web scraper code--------------------------------------------------
inp=input("Enter the url= ")
req=requests.get(inp)
soup=BeautifulSoup(req.content,"html.parser")
res=soup.title
res=res.get_text()
bdy=soup.body
bd=bdy.get_text()
read=res+bd
text=read
lowercase=text.lower()

#----------------to clean and tokenized the data extracted from URL------------------

clean_text=lowercase.translate(str.maketrans('','',string.punctuation))
tokenized_word=nltk.word_tokenize(clean_text,"english")

#---------------to clean the data from stop words-----------------------------------
final_word=[]
stopwords=[]
r1=open("StopWords_Auditor.txt","r").read()
r2=open("StopWords_Generic.txt","r").read()
r3=open("StopWords_Currencies.txt","r").read()
r4=open("StopWords_DatesandNumbers.txt","r").read()
r5=open("StopWords_GenericLong.txt","r").read()
r6=open("StopWords_Geographic.txt","r").read()
r7=open("StopWords_Names.txt","r").read()
r8=r1+" "+r2+" "+r3+" "+r4+" "+r5+" "+r6+" "+r7
stop_tokenized_word=nltk.word_tokenize(r8,"english")
for i1 in stop_tokenized_word:
        stopwords.append(i1)
for word in tokenized_word:
    for sw1 in stopwords:
        if sw1 in word:
            final_word.append(word)

#-------------------to get positive score-------------------------------------------
poscount=0
pos=open("positive-words.txt","r").read()
pos_tokenized_word=nltk.word_tokenize(pos,"english")
for fw1 in final_word:
    for pos1 in pos_tokenized_word:
        if pos1 in fw1:
            poscount+=1
print("Positive Score= ",poscount)


#--------------------to get negetive score------------------------------------------
negcount=0
neg=open("negative-words.txt","r").read()
neg_tokenized_word=nltk.word_tokenize(neg,"english")
for fw2 in final_word:
    for neg1 in neg_tokenized_word:
        if neg1 in fw2:
            negcount-=1
negetcount=negcount*-1
print("Negetive Score= ",negetcount)


#--------------------to get polarity score-----------------------------------------

ps=(poscount-negetcount)/((poscount+negetcount)+0.000001)
print("Polarity Score= ",ps)

#---------------------to get subjectivity score-----------------------------------

final_word2=len(final_word)
ss=(poscount+negetcount)/((final_word2)+0.000001)
print("Subjectivity Score= ",ss)

#------To calculate Average sentence length-------------------
str1=" "
final_word3=str1.join(final_word)
numword=textstat.lexicon_count(final_word3, removepunct=True)#lexicon_count used to count words from sentence
print("word count= ",numword)
numsent=textstat.sentence_count(text)
asl=numword/numsent
print("Average Sentence Length= ",asl)

#-------------------Average number of words per sentence-----------------------------

anwps=numword/numsent
print("Average number of words per sentence= ",anwps)

#-------Percentage of complex words------------------------------
for final_word4 in final_word:
    complex_words=textstat.polysyllabcount(final_word4)
print("complex word count= ",complex_words)
Percentage=(complex_words/numword)*100
print("Percentage of complex words= ","{:.2f}".format(Percentage),"%")

#----------Fog index----------------------------

Fog_index=0.4*(asl+Percentage)
print("Fog_index= ",Fog_index)

#--------count number of syllable-----------------------
n=final_word
a=[]
b="aeiouAEIOU"
for t in n:
    x=t.endswith("es")
    y=t.endswith("ed")
    if x is True:
        z=t.strip("es")
        a.append(z)
    elif y is True:
        v=t.strip("ed")
        a.append(v)
    else:
        a.append(t)
str2=" "
text2=str2.join(a)
syll=textstat.syllable_count(text2)
print("syllable count= ",syll)

#-----------------Average word length-----------------------------
m=final_word
str3=" "
text3=str3.join(m)
ccount=textstat.char_count(text3, ignore_spaces=True)
awl=ccount/numword
print("Average Word Length= ",awl)

#------------Personal Pronounce-------------------------------------
count=0
per=["I","we","my","ours","us"]
for p in final_word:
    if p !="US":
        for q in per:
            x1=re.search(q,p)
            if x1:
                count+=1
print("Personal Pronounce count= ",count)
    
