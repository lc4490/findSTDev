#! /Users/leonardo01px2020/opt/anaconda3/bin/python
import requests
import pandas as pd
import numpy as np
import re
pd.options.display.float_format = '{:5,.2f}'.format

def findSTDev(name, year):
    #Extract URL
    iteration = "01"
    first, last = name.lower().rstrip().split(" ")
    first = re.sub(r'\W+', '', first)
    last = re.sub(r'\W+', '', last)
    if(len(last)>5):
        last = last[:5]
    html = ""
    while(True):
        url = 'https://www.basketball-reference.com/players/' + last[0] + '/' + last + first[:2] + iteration + '/gamelog/' + str(year)
        temp = requests.get(url)
        if(name.lower() in temp.text.lower()):
            html = temp.content
            break
        else:
            temp2 = int(iteration)+1
            if(temp2 < 10):
                iteration = "0" + str(temp2)
            else:
                iteration = str(temp2)
    
    df_list = pd.read_html(html)
    df = df_list[-1]
    
    #Filter only counting stats
    df = df.filter(items=['FG','FGA','FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF','PTS', 'GmSc','+/-'])
    df = df[pd.to_numeric(df['FG'], errors='coerce').notnull()]
    df[df.columns] = df[df.columns].astype(float)
    
    #Find Standard Deviation of counting stats
    mean = (pd.DataFrame(df.mean()).transpose())
    std = (pd.DataFrame(df.std()).transpose())
    print("\n"+name,year,"\n\nMean Stats:\n", mean, "\n\nStandard Deviation Stats:\n",std)


name = input("Enter the name of the player: ")
year = input("Enter the season: ")
if(len(year) > 4):
    year = year[-4:]
findSTDev(name, year)
