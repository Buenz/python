import os, pandas as pd, numpy as np

#########functions

def post(x, y):  #x short, y long
    df=pd.DataFrame(x)
    df[1]=0
    num=0
    num2=0
    mult=1
    prev=0
    next1=0
    while True:
        if num==len(x):
            num=0
            num2+=1
            prev=num
            next1=num+1
        if x[num]==y[num2]:
            df.loc[num,1]+=1
            num2+=1
            prev=num
            next1=num+1
        elif x[num]!=y[num2] and num==next1:
            num2+=1
        elif x[num]!=y[num2] and num==prev:
            num+=1
        if num2>len(y)-1:
            break
    for i in range(len(df[0])):
        mult=mult*df[1][i]
    return mult

def top(x,y):
    check=post(x,y)
    if check<100000:
        return format(check, '05d')
    else:
        return 99999

###########Main

dirpath = os.getcwd()
print("Current directory is the following: " + dirpath)
g=input("Please insert path to file + file.txt: ")
srch=input("Please patter you want to search: ")

sq=pd.read_csv(g, header=None)

for i in range(sq.shape[0]):
    sq[0][i]=list(sq[0][i])

#srch= "join the nmi team"
sq2=list(' '.join(srch.split()))

sq[1]=0

for i in range(len(sq[1])):
    print(f"Level {i+1}: {top(sq2,sq[0][i])}")
