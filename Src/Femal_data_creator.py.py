# Import Module
import os

# Folder Path
path = "female_TC2Meas_txt"
# this code returns a female dataset iterating through nomo_female_3d body measurements
# Change the directory
os.chdir(path)

file_list=[]

# iterate through all files in current directory
for file in os.listdir():
	# Check whether file is in text format or not
	if file.endswith(".txt"):
		file_path = f"C:/Users/SAI/Downloads/NOMO-3d-400-scans_and_tc2_measurements/NOMO-3d-400-scans_and_tc2_measurements/nomo-scans/female_TC2Meas_txt/female_TC2Meas_txt/{file}"
		file_list.append(file_path)
	#print(file_list)
print(len(file_list))
file = open(file_list[0] , "r")

#creating the dataset

text = ""
newfile = open("Female_data.csv" , "a")
for i in file.readlines():
        text =text + i[0:i.index("=")]+","

text = text+'file_path'

text = text[:-1]+"\n"



for i in range(len(file_list)):     
        with open(file_list[i],'r') as file:
                for j in file.readlines():
                        text = text+j[j.index('=')+1:-1]+","
                text = text+file_list[i]
                text = text[:-1]+"\n"
                

with open("Female_data.csv","a") as a:
        a.write(text)
        a.close()
        

                
                
        
        
                
                
                
        
        
