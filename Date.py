import random
from datetime import date
t = date.today()

day=t.day
Library_ex=["New Year's Party ","Valentine's Dinner","Carnival Night","Karaoke Night ","Kayaking Trip ","Seaside Picnic","Halloween Party","Thanksgiving Jamboree ","Christmas Dinner","New Year's Party ","Valentine's Dinner","Carnival Night"]
List_m=[1,2,3,4,5,9,10,11,12,1,2,3]
List_d=[13,14,1,18,5,15,31,26,18]
month=11
day=20
print(month,day)
i=0
while i>=0:
    if month>List_m[i]:
        i=i+1
    else:
        break
if month > List_m[i]:
    print(Library_ex[i],Library_ex[i+1],Library_ex[i+2])
else:
    if day>=List_d[i]:
        print(Library_ex[i+1],Library_ex[i+2],Library_ex[i+3])
    else:
        print(Library_ex[i],'\n', Library_ex[i+1],'\n',Library_ex[i+2])
