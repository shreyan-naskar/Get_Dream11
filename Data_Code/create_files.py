import pandas as pd
import numpy as np
import random as rd
import os
from random import uniform as un
from random import randint as rd

Match_data_v4 = pd.read_csv("Matches.csv")
Batters = pd.read_csv("Batters.csv")
Bowlers = pd.read_csv("Bowlers.csv")
Bat_data = pd.read_csv("Batsmen_data.csv")
Bowl_data = pd.read_csv("Bowlers_data.csv")

Match_data_v4.drop(["Unnamed: 0"], inplace = True, axis = 1)
Bat_data.drop(['Unnamed: 0.1', 'Unnamed: 0', 'Span', 'NO','Unnamed: 15'], inplace = True, axis = 1)
Bowl_data.drop(['Unnamed: 0.1', 'Unnamed: 0', 'Span', 'BBI','Unnamed: 14'], inplace = True, axis = 1)


# Functions

# for bat and ball lists
def format_name(name):
  L = name.split()
  new = L[0][0] + ' ' + L[-1]
  return new

# for role column in matchi.csv
def Role(name, Batters, Bowlers):
    Bat, Bowl = [], []
    for i in Batters.values:
       Bat.append(i[1])
    for i in Bowlers.values:
       Bowl.append(i[1])
    if name in Bat:
       return "Batsman"
    if name in Bowl:
       return "Bowler"     

# bat data extract
def fetch_bat(bat,name):
  #stats = [0:'Player',1:'Mat',2:'Inns',3:'Runs',4:'HS',5:'Ave',6:'BF',:7'SR',8:'100',9:'50',:10'0',11:'4s',12:'6s']
  val = [0 for i in range(len(bat[0]))]
  val[0] = name
  val[1] = float(rd(33,57))
  val[2] = float(val[1] - rd(4,7))
  val[3] = float(val[2]*rd(31,39))
  val[4] = float(rd(42,76))
  val[5] = round(un(23.42,42.59),2)
  val[6] = float(val[2]*rd(23,29))
  val[7] = np.round(float(val[3]/val[6])*100,2) #Runs/BF
  val[8] = 0.0
  val[9] = float(rd(0,7))
  val[10] = float(rd(0,9))
  val[11] = float(rd(74,103))
  val[12] = float(rd(39,55))
  
  for i in bat:
    if name == i[0] and '-' not in i:
      val = i
  return val

# bowl data extract
def fetch_bowl(bowl,name):
  #stats = [0:'Player',1::'Mat',2:'Inns',3:'Overs',4:'Mdns',5:'Runs',6:'Wkts',7:'Ave',8:'Econ',9:'SR',10:'4',11:'5']
  val = [0 for i in range(len(bowl[0]))]
  val[0] = name
  val[1] = float(rd(37,63))
  val[2] = float(val[1] - rd(3,5))
  val[3] = float(val[2]*rd(3,4))
  val[4] = float(rd(0,4))
  val[5] = float(val[3]*rd(6,17))
  val[6] = float(rd( (val[2] - rd(12,17)),(val[2] + rd(15,21)) ))
  val[7] = np.round(float(val[5]/val[6]),2)
  val[8] = np.round(float(val[5]/val[3]),2)
  val[9] = np.round(float(val[3]*6/val[6]))
  val[10] = float(rd(0,3))
  val[11] = float(rd(0,1))

  for i in bowl:
    if name == i[0]:
      val = i
  return val  

# make seperate directory for batter match data
def bat_mkdir():
   directory = "Batter Match Data"
   parent_dir = "C:/Users/SHREYAN/Desktop/Programs/Python/Proj/"
   
   path = os.path.join(parent_dir, directory)
   os.mkdir(path)

   return path

# make seperate directory for bowler match data
def bowl_mkdir():
   directory = "Bowler Match Data"
   parent_dir = "C:/Users/SHREYAN/Desktop/Programs/Python/Proj/"
   
   path = os.path.join(parent_dir, directory)
   os.mkdir(path)

   return path    
 
#create datasets
def create_datasets(Match_data_v4, bat, bowl, dir_bat, dir_bowl):
    data = []
    for i in Match_data_v4.values:
        data.append(i)
    #print(data)
    for i in range(len(data)):
        rows_bat, rows_bowl, role = [],[],[]
        team1 = data[i][1].split(",")
        team2 = data[i][2].split(",")

        for j in range(len(team1)):
            r = Role(team1[j], Batters, Bowlers)
            if r == "Batsman":
               item = fetch_bat(bat, team1[j])
               item = np.append(item,0)
               rows_bat.append(item)
            elif r == "Bowler":
               item = fetch_bowl(bowl, team1[j])
               item = np.append(item,0)
               rows_bowl.append(item)
               

        for j in range(len(team2)):
            r = Role(team2[j], Batters, Bowlers)
            if r == "Batsman":
               item = fetch_bat(bat, team2[j])
               item = np.append(item,0)
               rows_bat.append(item)
            elif r == "Bowler":
               item = fetch_bowl(bowl, team2[j])
               item = np.append(item,0)
               rows_bowl.append(item)
               

        filename_bat = dir_bat + "/Match" + str(i) + "Bat.csv"
        filename_bowl = dir_bowl + "/Match" + str(i) + "Bowl.csv"
        bat_header = ['Player','Mat','Inns','Runs','HS','Ave','BF','SR','100','50','0','4s','6s','IsInD11']
        bowl_header = ['Player','Mat','Inns','Overs','Mdns','Runs','Wkts','Ave','Econ','SR','4','5','IsInD11']

        Bat_df = pd.DataFrame(data = rows_bat, columns = bat_header)
        Bowl_df = pd.DataFrame(data = rows_bowl, columns = bowl_header)

        Bat_df.to_csv(filename_bat)
        Bowl_df.to_csv(filename_bowl)




# main



# bat data and conversion to floats
bat = []
for i in Bat_data.values:
  i[0] = format_name(i[0])
  bat.append(i)

n = len(bat[0])
for i in range(len(bat)):
  if '-' not in bat[i]:
    for j in range(n):
      if j not in (0,4):
        bat[i][j] = float(bat[i][j])
      elif j==4:
        bat[i][j] = float(bat[i][j].rstrip("*"))

# bowl data and conversation to floats
bowl = []
for i in Bowl_data.values:
  i[0] = format_name(i[0])
  bowl.append(i)

n = len(bowl[0])
for i in range(len(bowl)):
  if '-' not in bowl[i]:
    for j in range(1,n):
      bowl[i][j] = float(bowl[i][j])


bat_dir = bat_mkdir()
bowl_dir = bowl_mkdir() 

create_datasets(Match_data_v4, bat, bowl, bat_dir, bowl_dir)

#Match0.csv ->latest 2022 final
#Match372.csv ->oldest 2017 final