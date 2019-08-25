import os, pandas as pd, math

dirpath = os.getcwd()
print("Current directory is the following: " + dirpath)

g=input("Please insert path to file + file.txt: ")

print("Please see minimum price below:\n")

#g="/Users/harrisonbueno/Desktop/NMI/product_costs.txt"

file_txt=pd.read_csv(g, sep=" ", header=None)

for i in range(file_txt.shape[0]):
    print(f"Line {i+1}: {int(math.ceil(file_txt[0][i]/(1-file_txt[1][i])))}")
