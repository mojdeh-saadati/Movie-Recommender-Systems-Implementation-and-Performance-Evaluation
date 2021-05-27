
import imdb
import csv
import sys
import importlib
#importlib.reload(sys)
from importlib import reload
from imdb import IMDb
from idlelib.idle_test.mock_tk import Mbox
mbObj = imdb.IMDb()
Table = [[0 for x in range(13)] for y in range(2769)] 
Table[0][0] = "userID"; Table[0][1] = "watchedImdbID"; Table[0][2] = "newMovieImdbID";  Table[0][3] = "year";
Table[0][4] = "genre"; Table[0][5] = "imdbRating";Table[0][6] = "country";Table[0][7] = "director";Table[0][8] = "movieName";
Table[0][9] = "firstActor";Table[0][10] = "Keywords";



with open('C:\\Users\\Mojdeh Saadati\\Desktop\\CleanData.csv','r',encoding="utf-8") as inf5:
    reader5 = csv.reader(inf5, delimiter=',')
    c = 0;
    for row in reader5:
        if(c == 0):
            c = c+1;
            continue
        if(c >= 501):
            break;
        
   #     print(row[1])
        listObj = mbObj.get_movie_recommendations(row[1])
        obj = listObj['data']['recommendations']['database']
        for ob in obj[0:3]:
            print(ob)
            print("---")
            Table[c][0] = row[0];Table[c][1] = row[1];
            Table[c][2] =ob.movieID;
            movieObj = mbObj.get_movie(ob.movieID)
            Table[c][3] = movieObj['year']  
            Table[c][4] = movieObj['genres']
            Table[c][5] = movieObj['rating']
            Table[c][6] = movieObj['country']
#            print("fearures")
#            print(c)
            temp = movieObj['director']
            Table[c][7] = [temp[0]['name']]
            Table[c][8] = movieObj['title']
            cast = movieObj['cast']
            Table[c][9] = [cast[0]['name'],cast[1]['name']]
            Table[c][10] = mbObj.get_movie_keywords(Table[c][1])         
  #          print(Table)
            c = c+1; 
            print("c==")
            print(c)

with open('C:\\Users\\Mojdeh Saadati\\Desktop\\dataset2.csv','w') as temp:        
    writer = csv.writer(temp)
    for r in Table: 
        writer.writerow(r)
       