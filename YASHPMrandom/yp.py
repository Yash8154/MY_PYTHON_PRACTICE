# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:15:04 2022

@author: Mehta Yash
"""

"""
Code Challenge
icccricket_SQLite.py

Scrap the data from the URL below and store in mySQL database
https://www.icc-cricket.com/rankings/mens/team-rankings/odi
"""


from bs4 import BeautifulSoup
import requests

#Get Source Code of page
url = "https://www.icc-cricket.com/rankings/mens/team-rankings/t20i"
source = requests.get(url).text

#Parsing of HTML data
soup = BeautifulSoup(source,"lxml")

#Get table from html data
ranking_table = soup.find('table', class_='table')


import sqlite3

# connecting database
conn = sqlite3.connect ( 'ICC_cricket.db' )
# creating cursor
c = conn.cursor()

# creating table of student
c.execute ("""CREATE TABLE ranking(
              rank INTEGER,
              team TEXT,
              weighted_matches INTEGER,
              points INTEGER,
              rating INTEGER
          )""")
conn.commit()

for row in ranking_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        rank = int(cells[0].text.strip())
        team = cells[1].text.strip()
        weighted_matches = int(cells[2].text.strip())
        points = int(cells[3].text.strip().replace(",",""))
        rating = int(cells[4].text.strip().replace(",",""))
        c.execute("INSERT INTO ranking VALUES({},'{}',{},{},{})".format(rank,team,weighted_matches,points,rating))
        conn.commit()
        
# Retriving data from database
c.execute("SELECT * FROM ranking")

from pandas import DataFrame
df = DataFrame(c.fetchall())  
df.columns = ["Rank","Team","Weighted Matches","Points","Rating"]
print(df)

c.execute("DROP Table ranking")
conn.commit()

conn.close()















