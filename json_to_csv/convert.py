from json_to_csv import *
import glob

#json_to_csv("dataset/a-57.json", "dataset/a-57.csv")

directory_name = 'dataset/'

files = glob.glob(directory_name + '*')
ctr = 0
for f in files:
	ctr= ctr+1
	try:
		print(str(ctr)+" csvfiles/"+f+".csv")
		json_to_csv(f, "csvfiles/"+f+".csv")
	except Exception:
		print(str(ctr) + 'ERROR '+f)

