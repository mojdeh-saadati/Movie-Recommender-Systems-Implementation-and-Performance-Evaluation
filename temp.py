
import imdb
import csv
import sys
import importlib
#importlib.reload(sys)
from importlib import reload
from imdb import IMDb
from idlelib.idle_test.mock_tk import Mbox
mbObj = imdb.IMDb()
listObj = mbObj.get_movie_recommendations(114746)
print(listObj)
obj = listObj['data']['recommendations']['database']
print(obj)
