
import imdb
import csv
import sys
import importlib
from imdb import IMDb
iaa = IMDb()
"""
Table = [[0 for x in range(2)] for y in range(200)] 
#Table[0][2] = "newMovieImdbID";  Table[0][3] = "year";
#Table[0][4] = "genre"; Table[0][5] = "imdbRating";Table[0][6] = "country";Table[0][7] = "director";Table[0][8] = "movieName";
#Table[0][9] = "firstActor";


c = 0;
# get a movie and print its director(s)

with open('C:\\Users\\Mojdeh Saadati\\Desktop\\contentBaseMethodDatabase2.csv','r',encoding="utf-8") as inf5:
    reader5 = csv.reader(inf5, delimiter=',')
    for row in reader5:
        movie = iaa.get_movie(row[0])
        Table[c][0] = movie['year']  
        c = c+1;
inf5.close()        

with open('C:\\Users\\Mojdeh Saadati\\Desktop\\contentBaseMethodDatabase2.csv','r',encoding="utf-8") as inf5:
    reader5 = csv.reader(inf5, delimiter=',')
    for row in reader5:
        movie = iaa.get_movie(row[0])
        temp = movie['genres']  
        for e in temp:
            Table[c][0] = e;
            c = c+1;
inf5.close()

with open('C:\\Users\\Mojdeh Saadati\\Desktop\\contentBaseMethodDatabase2.csv','r',encoding="utf-8") as inf5:
    reader5 = csv.reader(inf5, delimiter=',')
    for row in reader5:
        movie = iaa.get_movie(row[0])
        Table[c][0] = movie['rating']  
        c = c+1;
inf5.close()

with open('C:\\Users\\Mojdeh Saadati\\Desktop\\contentBaseMethodDatabase2.csv','r',encoding="utf-8") as inf5:
    reader5 = csv.reader(inf5, delimiter=',')
    for row in reader5:
        movie = iaa.get_movie(row[0])
        temp = movie['country']  
        for e in temp:
            Table[c][0] = e;
            c = c+1;
inf5.close()



    
with open('C:\\Users\\Mojdeh Saadati\\Desktop\\contentBaseMethodDatabase2.csv','r',encoding="utf-8") as inf5:
    reader5 = csv.reader(inf5, delimiter=',')
    for row in reader5:
        movie = iaa.get_movie(row[0])
        temp = movie['director']  
        Table[c][0] = temp[0].personID
        c = c+1;
inf5.close()

with open('C:\\Users\\Mojdeh Saadati\\Desktop\\contentBaseMethodDatabase2.csv','r',encoding="utf-8") as inf5:
    reader5 = csv.reader(inf5, delimiter=',')
    for row in reader5:
        movie = iaa.get_movie(row[0])
        temp = movie['cast']  
        Table[c][0]= temp[0].personID
        c = c+1;
inf5.close()

with open('C:\\Users\\Mojdeh Saadati\\Desktop\\contentBaseMethodDatabase3.csv','w') as temp:        
    writer = csv.writer(temp)
    for r in Table: 
        writer.writerow(r)
temp.close();
"""
################################################################
Table2 = [[0 for x in range(200)] for y in range(20)] 
c = 1;

with open('C:\\Users\\Mojdeh Saadati\\Desktop\\contentBaseMethodDatabase2.csv','r',encoding="utf-8") as inf5:
    reader5 = csv.reader(inf5, delimiter=',')
    for row in reader5:
        Table2[c][0]= row[0]
        c = c+1;
        if(c > 15):
            break;
inf5.close()

c = 1;
with open('C:\\Users\\Mojdeh Saadati\\Desktop\\contentBaseRowNames.csv','r',encoding="utf-8") as inf5:
    reader5 = csv.reader(inf5, delimiter=',')
    for row in reader5:
        print(row)
        Table2[0][c]= row[0]
        if(c > 64):
            break;
        print(c)
        c = c+1;
inf5.close()

print("varede bakhsh dovom shod")
c =0;
for row in Table2:
    if(c ==0 ):
        c = c+1;
        continue;
    if(c > 15):
        break;
    movie = iaa.get_movie(row[0])
    if(row[0] == 0):
        break; # it means we finished all movies. 
    
    temp= movie['year']
    print(temp)  
    d = 0;
    for d in range(64):
        print(str(temp) )
        print(Table2[0][d])
        print(d)
        if(Table2[0][d] == str(temp)):
            print("booofgh")
            Table2[c][d] = 1;
            break;
    print("finished year")
    print(c)
    temp= movie['rating']  
    d= 0;
    for d in range(64):
        if(Table2[0][d] == str(temp)):
            Table2[c][d] = 1;
            break;
        d = d+1
        
    temp = movie['genres']  
    for e in temp:
        d = 0;
        for d in range(64):
            if(Table2[0][d] == e):
                Table2[c][d] = 1;
                break;
            d = d+1
            
    temp = movie['country']  
    for e in temp:
        d = 0;
        for d in range(64):
            if(Table2[0][d] == e):
                Table2[c][d] = 1;
                break;
            d = d+1

    temp = movie['director']  
    temp = temp[0].personID
    d= 0;
    for d in range(64):
        if(Table2[0][d] == str(int(temp))):
            Table2[c][d] = 1;
            break;
        d = d+1

                    
    temp = movie['cast']  
    temp = temp[0].personID
    d= 0;
    
    for d in range(64):
        print(Table2[0][d])
        print(str(int(temp)))
        if(Table2[0][d] == str(int(temp))):
            Table2[c][d] = 1;
            break;
        d = d+1
            
    c = c+1;   
        
with open('C:\\Users\\Mojdeh Saadati\\Desktop\\contentBaseMethodDatabase4.csv','w') as temp:        
    writer = csv.writer(temp)
    for r in Table2: 
        writer.writerow(r)
temp.close();

print(Table2)

