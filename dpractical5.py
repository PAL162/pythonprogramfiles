'''Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''


d = {1: 10, 2: 20}
dd = {3: 30, 4: 40}
ddd = {5: 50, 6: 60}
dddd = {}
for v in (d, dd, ddd): #it will copy in v
    dddd.update(v)     #it will update ddd
print(dddd)

#Khant Pal_D21CE162