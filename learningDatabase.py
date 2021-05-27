
import imdb
import csv
import sys
import importlib
#importlib.reload(sys)
from importlib import reload

# adding movie id to training dataset. 
Table = [[0 for x in range(13)] for y in range(923)] # I have to fix this part later. 
Table[0][0] = "userID"; Table[0][1] = "imdbId"; Table[0][2] = "userRating";  Table[0][3] = "year";
Table[0][4] = "genre1";Table[0][5] = "genre2";Table[0][6] = "genre3"; Table[0][7] = "genre4";
Table[0][8] = "imdbRating";Table[0][9] = "country1";Table[0][10] = "country2"; Table[0][11] = "directorID";
Table[0][12] = "mainActorID";
c = -1;
with open('C:\\Users\\Mojdeh Saadati\\Desktop\\MovieLenDataset1.csv','r',encoding="utf-8") as inf:
    reader = csv.reader(inf, delimiter=',')
    for row in reader:
        c = c+1
        Table[c][0] = row[0]
        Table[c][2] = row[2]
        with open('C:\\Users\\Mojdeh Saadati\\Desktop\\ml-20m\\ml-20m\\links.csv','r',encoding="utf-8") as inf2:
            reader2 = csv.reader(inf2, delimiter=',')
            for row2 in reader2:
                if row[1] == row2[0]:
                    Table[c][1] = row2[1]
                    Table[c][11] = row2[0]
                    break
print(Table)                
# adding tags!                 
""" c = 0;
for row in Table:
    if(row[1] == 'imdbId'):
        continue
    if(int(row[11]) == 0):
        break;
  #  print(int(row[11]))
    with open('C:\\Users\\Mojdeh Saadati\\Desktop\\ml-20m\\ml-20m\\newtags.csv','r',encoding="ISO-8859-1") as inf3:
         reader3 = csv.reader(inf3, delimiter=',')
         for row3 in reader3:
             if(row3[0] == 'movieId'):
                 continue
             if(row3[0] == ''):
                 break            
             if int(row[11]) == int(row3[0]):
                 Table[c+1][10] = row3[1]
                # print(row3[1])
                 break
             
    c = c+1;         
print("create database by adding IMDB database")               
"""
####################################################################
####        Create Database by adding IMDB database
####################################################################
from imdb import IMDb
mbObj = imdb.IMDb()
c = 0;
print("table[1][1]")

for row in Table:
    if(c == 0):
        c = c+1;
        continue;
    if(c < 500):
        c = c+1; 
        continue;
    if(c == 530 or c == 575):
        c = c+1;
        continue;
    if(c >= 921):
        c = c+1;
        break;
    
        
    print("c==")
    print(c)
    print(Table[c][1])
    movieObj = mbObj.get_movie(Table[c][1]) 
    print(movieObj.summary)
    
    Table[c][3] = movieObj['year']  
    strTemp = movieObj['genres']
    Table[c][4] = 0 ;Table[c][5] = 0 ;Table[c][6] = 0 ;Table[c][7] = 0 ; 
    d = 0;
    if("Action" in strTemp and d <= 3 ):
        Table[c][4+d] = 1; 
        d = d+1;
    if("Adventure" in strTemp and d <= 3 ):
        Table[c][4+d] = 2;
        d = d+1;
    if("Family" in strTemp and d <= 3 ):
        Table[c][4+d] = 3;
        d = d+1;
    if("Fantasy" in strTemp and d <= 3 ):
        Table[c][4+d] = 4;
        d = d+1;
    if("Thriller" in strTemp and d <= 3 ):
        Table[c][4+d] = 5; 
        d = d+1;  
    if("Sci-Fi" in strTemp  and d <= 3 ):
        Table[c][4+d] = 6;
        d = d+1;
    if("Mystery" in strTemp and d <= 3 ):
        Table[c][4+d] = 14;
        d = d+1;
    if("Crime" in strTemp and d <= 3 ):
        Table[c][4+d] = 7;
        d = d+1;
    if("Drama" in strTemp and d <= 3 ):
        Table[c][4+d] = 8;  
        d = d+1;                      
    if("Comedy" in strTemp and d <= 3 ):
        Table[c][4+d] = 9;   
        d = d+1;                     
    if("Biography" in strTemp and d <= 3 ):
        Table[c][4+d] = 10;
        d = d+1;                        
    if("History" in strTemp and d <= 3 ):
        Table[c][4+d] = 11;   
        d = d+1;                     
    if("Horror" in strTemp and d <= 3 ):
        Table[c][4+d] = 12;     
        d = d+1;                   
    if( ("Musical" in strTemp or "Music" in strTemp) and d <= 3 ):
        Table[c][4+d] = 13;                        
        d = d+1;
    if("War" in strTemp and d <= 3 ):
        Table[c][4+d] = 14;                        
        d = d+1;
    if("Western" in strTemp and d <= 3 ):
        Table[c][4+d] = 15;                        
        d = d+1;
    if("Romance" in strTemp and d <= 3 ):
        Table[c][4+d] = 16;                        
        d = d+1;
    if("Animation" in strTemp and d <= 3 ):
        Table[c][4+d] = 17;                        
        d = d+1;           
                                 
    Table[c][8] = movieObj['rating']
    strTemp = movieObj['country']
    d = 0;
    if("USA" in strTemp and d <= 1 ):
        Table[c][9+d] = 1;                        
        d = d+1;    
    if("France" in strTemp and d <= 1 ):
        Table[c][9+d] = 2;                        
        d = d+1;    
    if("Germany" in strTemp and d <= 1 ):
        Table[c][9+d] = 3;                        
        d = d+1;    
    if("Spain" in strTemp and d <= 1 ):
        Table[c][9+d] = 4;                        
        d = d+1;    
    if("Belgium" in strTemp and d <= 1 ):
        Table[c][9+d] = 5;                        
        d = d+1;    
    if("Hong Kong" in strTemp and d <= 1 ):
        Table[c][9+d] = 6;                        
        d = d+1;    
    if("UK" in strTemp and d <= 1 ):
        Table[c][9+d] = 7;                        
        d = d+1;    
    if("Italy" in strTemp and d <= 1 ):
        Table[c][9+d] = 8;                        
        d = d+1;    
    if("Japan" in strTemp and d <= 1 ):
        Table[c][9+d] = 9;                        
        d = d+1;    
    if("China" in strTemp and d <= 1 ):
        Table[c][9+d] = 10;                        
        d = d+1;    
    if("Canada" in strTemp and d <= 1 ):
        Table[c][9+d] = 11;                        
        d = d+1;    
    if( ("Australi" in strTemp or "New Zealand" in strTemp  ) and d <= 1 ):
        Table[c][9+d] = 12;                        
        d = d+1;    
    if("Taiwan" in strTemp and d <= 1 ):
        Table[c][9+d] = 13;                        
        d = d+1;            
        
    temp = movieObj['director']
    print("director")
    print(temp[0].personID)
    Table[c][11] = temp[0].personID
    print(movieObj.get_current_info())
    print("imdbId")
    print(Table[c][1])
    cast = movieObj['cast']
    print(cast)
    Table[c][12] = cast[0].personID
    print(Table[c])
    c = c+1;
    

with open('C:\\Users\\Mojdeh Saadati\\Desktop\\neuralNetworkDatabase.csv','w') as temp:        
    writer = csv.writer(temp)
    for r in Table: 
        writer.writerow(r)

######################################################################    
######             learn neural network
######################################################################        
    
######################################################################    
######             Do Beam Search
######################################################################        
