#!/usr/bin/env python3

# Import the imdb package.
import imdb
import csv
import sys
import importlib
#importlib.reload(sys)
from importlib import reload
#reload(sys)
#sys.setdefaultencoding('utf-8')
#sys.set
#from tkinter.tix import ROW
#print("enter the movie name")

storev=[]
storeimdb=[]

words=input("enter the movie name\n").lower()
print(words)
with open('C:\\Users\\Mojdeh Saadati\\Desktop\\ml-20m\\ml-20m\\movies.csv','r',encoding="utf-8") as inf:
    reader = csv.reader(inf, delimiter=',')

    for row in reader:
        if words in row[1].lower():
                #print(row)
                nl=row[0]
                storev.append(nl)   
                print("storev")
                print(row[0])
                print(row[1])     
      #print(header)

#print(storev[7])
print("length of first list is:")
print(len(storev))
with open('C:\\Users\\Mojdeh Saadati\\Desktop\\ml-20m\\ml-20m\\links.csv','r',encoding="utf-8") as inf2:
    reader2 = csv.reader(inf2, delimiter=',')

    for row1 in reader2:
        if row1[0] in storev:
                #print(row1)
                nl2=row1[1]
                storeimdb.append(nl2)
      
#dates=readmyfile('/Ussers/Shaiqur/downloads/ml-20m/movies.csv')
#print(storeimdb)
print("length of second list")
print(len(storeimdb))
# Create the object that will be used to access the IMDb's database.
ia = imdb.IMDb() # by default access the web.
for rm in storeimdb:
 the_matrix = ia.get_movie(rm)
 #print(the_matrix['movie'])
 print(the_matrix)
 actors=the_matrix['actors']
 print(actors[0]) 

 ###########################
from imdb import IMDb
iaa = IMDb()

# get a movie and print its director(s)
the_matrix = iaa.get_movie('0133093')
print(the_matrix['director'])
result = iaa.search_movie("frozen")
the_unt = result[0]
iaa.update(the_unt)
# Print some information.

print(the_unt.summary())
print(the_unt['rating'])
print(the_unt)

# show all the information sets avaiable for Movie objects



