# # Plotting functions


import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt

# def Plotvec1(u, z, v):
    
#     ax = plt.axes() # to generate the full window axes
#     ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
#     plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
#     ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
#     plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
#     ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
#     plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
#     plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
#     plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

  
# # Example vectors
# u = np.array([1, 0])
# v = np.array([0, 1])
# z = u + v

# # Call the function
# Plotvec1(u, z, v)

# # Display the plot
# plt.show()


# X=np.array([[1,0],[0,1]])
# Y=np.array([[2,2],[2,2]])
# Z=np.dot(X,Y)
# print(Z)
# import pandas as pd
# from nba_api.stats.static import teams
# def one_dict(list_dict):
#     keys=list_dict[0].keys()
#     out_dict={key:[] for key in keys}
#     for dict_ in list_dict:
#         for key, value in dict_.items():
#             out_dict[key].append(value)
#     return out_dict

# nba_teams = teams.get_teams()
# nba_teams[0:3]
# dict_nba_team=one_dict(nba_teams)
# df_teams=pd.DataFrame(dict_nba_team)
# df_teams.head()
# # print(df_teams)
# df_warriors=df_teams[df_teams['nickname']=='Warriors']
# # print(df_warriors)

# id_warriors=df_warriors[['id']].values[0][0]
# print(id_warriors)

# from bs4 import BeautifulSoup # this module helps in web scrapping.
# table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
# soup = BeautifulSoup(table, 'html5lib')
# print(soup.prettify())

# table_rows=soup.find_all('tr')
# print(table_rows[0])


a=np.array([0,1,0,1,0]) 
b=np.array([1,0,1,0,1]) 
print(a/b)


