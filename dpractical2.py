#Write a Python script to merge two Python dictionaries.
d = {"1": 20, "2": 22, "3": 43} #dictionaries values
d2 = {"4": 50, "5": 42, "6": 63}
d1 = d.copy() #it copy value of d in d1
d1.update(d2) #it update d1
print(d1)

#Khant Pal_D21CE162