import pickle
import pandas as pd

# for role column of a player
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

# Fetch player data
def fetch_data(name, Batters, Bowlers, Bat_data, Bowl_data):
	role = Role(name, Batters, Bowlers)

	Bat, Bowl = [], []
	for i in Batters.values:
		Bat.append(i)
	for i in Bowlers.values:
		Bowl.append(i)

	if role == "Batsman":
		for i in Bat_data.values:
			if(i[0] == name):
				return i
	else:
		for i in Bowl_data.values:
			if(i[0] == name):
				return i


#make Bat and Bowl datasets
def make_datasets(Matches, Batters, Bowlers, Bat_data, Bowl_data, dir_bat, dir_bowl):
	data = []
	for i in Matches.values:
		data.append(i)
	#print(data)
	for i in range(len(data)):
		rows_bat, rows_bowl, role = [],[],[]
		team1 = data[i][0].split(",")
		team2 = data[i][1].split(",")

		for j in range(len(team1)):
			r = Role(team1[j], Batters, Bowlers)
			if r == "Batsman":
				item = fetch_data(team1[j], Batters, Bowlers, Bat_data, Bowl_data)
				#item = np.append(item,0)
				rows_bat.append(item)
			elif r == "Bowler":
				item = fetch_data(team1[j], Batters, Bowlers, Bat_data, Bowl_data)
				#item = np.append(item,0)
				rows_bowl.append(item)
               
		for j in range(len(team2)):
			r = Role(team2[j], Batters, Bowlers)
			if r == "Batsman":
				item = fetch_data(team2[j], Batters, Bowlers, Bat_data, Bowl_data)
				#item = np.append(item,0)
				rows_bat.append(item)
			elif r == "Bowler":
				item = fetch_data(team2[j], Batters, Bowlers, Bat_data, Bowl_data)
				#item = np.append(item,0)
				rows_bowl.append(item)
               
		filename_bat = dir_bat + "/Match_Bat.csv"
		filename_bowl = dir_bowl + "/Match_Bowl.csv"
		bat_header = ['Player','Mat','Inns','Runs','HS','Ave','BF','SR','100','50','0','4s','6s']
		bowl_header = ['Player','Mat','Inns','Overs','Mdns','Runs','Wkts','Ave','Econ','SR','4','5']

		Bat_df = pd.DataFrame(data = rows_bat, columns = bat_header)
		Bowl_df = pd.DataFrame(data = rows_bowl, columns = bowl_header)

		Bat_df.to_csv(filename_bat)
		Bowl_df.to_csv(filename_bowl)





file1 = "C:/Users/SHREYAN/Desktop/Programs/Python/Proj/Data_Code/Saved_models/bat_model.pickle"
Bat_model = pickle.load(open(file1,"rb"))

file2 = "C:/Users/SHREYAN/Desktop/Programs/Python/Proj/Data_Code/Saved_models/bowl_model.pickle"
Bowl_model = pickle.load(open(file2,"rb"))

Match_path = "C:/Users/SHREYAN/Desktop/Programs/Python/Proj/Data_Code/Test_Data/New_match.csv"
match = pd.read_csv(Match_path)

Batters = pd.read_csv("C:/Users/SHREYAN/Desktop/Programs/Python/Proj/Data_Code/Player_Data_GenCode/Batters.csv")
Bowlers = pd.read_csv("C:/Users/SHREYAN/Desktop/Programs/Python/Proj/Data_Code/Player_Data_GenCode/Bowlers.csv")
Bat_data = pd.read_csv("C:/Users/SHREYAN/Desktop/Programs/Python/Proj/Data_Code/Player_Data_GenCode/Batter_new_data.csv")
Bowl_data = pd.read_csv("C:/Users/SHREYAN/Desktop/Programs/Python/Proj/Data_Code/Player_Data_GenCode/Bowler_new_data.csv")

bat_dir = "C:/Users/SHREYAN/Desktop/Programs/Python/Proj/Data_Code/Test_Data"
bowl_dir = "C:/Users/SHREYAN/Desktop/Programs/Python/Proj/Data_Code/Test_Data"

make_datasets(match, Batters, Bowlers, Bat_data, Bowl_data, bat_dir, bowl_dir)