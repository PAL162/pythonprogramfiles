#Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
list=['Cars', 'Cars', 'Flowers', 'ball','Cats']
# Declare tuple
tuple = (1,2,3,4,5,1,3,1,1)
# Declare Dictionary
Car = {
     "Brand":"honda",
     "Model":"wrv",
     "Year":"2021",
     "Brand":"honda"
 }
# Logic
from collections import Counter
l = Counter(list)
l.most_common(1)
t = Counter(tuple)
t.most_common(1)
d = Counter(Car)
d.most_common(1)
# Print Common Element In List
print (" ", l.most_common(1))
# Print Common Element In Tuple
print (" ", t.most_common(1))
# Print Common Element In Dictionary
print (" ", d.most_common(1))

#Khant Pal_D21CE162