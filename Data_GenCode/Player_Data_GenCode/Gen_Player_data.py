import pandas as pd
import numpy as np
from random import uniform as un
from random import randint as rd

Batters = pd.read_csv("Batters.csv")
Bowlers = pd.read_csv("Bowlers.csv")
Bat_data = pd.read_csv("Batsmen_data.csv")
Bowl_data = pd.read_csv("Bowlers_data.csv")

# for bat and ball lists
def format_name(name):
  L = name.split()
  new = L[0][0] + ' ' + L[-1]
  return new

# List of Batsmen and Bowlers
def gen_data(Batters, Bowlers, Bat_data, Bowl_data):
	All_Bat, All_Bowl = [], []
	for i in Batters.values:
		All_Bat.append(i[1])	

	for i in Bowlers.values:
		All_Bowl.append(i[1])

	Bat_stat, Bat_header = [], Bat_data.columns
	for i in Bat_data.values:
		if '-' not in i:
			row = []
			for j in range(len(i)):
				if j == 0:
					row.append( format_name(i[j]) )
				elif j == 4:
					row.append(i[j].rstrip("*"))
				else:
					row.append(i[j])
			Bat_stat.append(row)


	Bowl_stat, Bowl_header = [], Bowl_data.columns
	for i in Bowl_data.values:
		if '-' not in i:
			row = []
			for j in range(len(i)):
				if j == 0:
					row.append( format_name(i[j]) )
				else:
					row.append(i[j])
			Bowl_stat.append(row)

	Have_bat = [i[0] for i in Bat_stat ]
	Have_bowl = [i[0] for i in  Bowl_stat ]


	# Generate data for batsmen with missing data
	for i in All_Bat:
		if i not in Have_bat:

			val = [0 for i in Bat_header]

			val[0] = i
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

			Bat_stat.append(val)


	# Generate data for bowlers with missing data
	for i in All_Bowl:
		if i not in Have_bowl:

			val = [0 for i in Bowl_header]

			val[0] = i
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

			Bowl_stat.append(val)

	Bat_df = pd.DataFrame(data = Bat_stat, columns = Bat_header)
	Bowl_df = pd.DataFrame(data = Bowl_stat, columns = Bowl_header)

	Bat_df.to_csv("Batter_new_data.csv")
	Bowl_df.to_csv("Bowler_new_data.csv")

gen_data(Batters, Bowlers, Bat_data, Bowl_data)
