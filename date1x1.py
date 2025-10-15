import random
from datetime import date
"""In this date problem we found we can't just simply use binary search due to some users' time(month-day) is not in list as a element, so I improved the binary search, now this algorithm can automatically search a range between two adjacency elements"""
"""but this is still not a perfect algorithm, it can't search range below the first element so I have to make a compromise add a 0 as a starting elements, future version may fix it"""
def event_recommend():
    t = date.today()
    day=t.day
    Library_ex=[0,"New Year's Party ","Valentine's Dinner","Carnival Night","Karaoke Night ","Kayaking Trip ","Seaside Picnic","Halloween Party","Thanksgiving Jamboree ","Christmas Dinner","New Year's Party ","Valentine's Dinner","Carnival Night"]
    List_m=[0,1.13,2.14,3.1,4.18,5.5,9.15,10.31,11.26,12.18]
    test_date=8.14
    low=0
    high=len(List_m)-1 #binary search
    while low<=high:
        mid= low + (high -low) // 2
        if high-low == 1 :
            print(mid,List_m[mid])
            if List_m[mid+1] > test_date: 
                print(Library_ex[mid+1],Library_ex[mid+2],Library_ex[mid+3])
                break
            else:
                print(Library_ex[mid+2],Library_ex[mid+3],Library_ex[mid+4])
                break
        elif List_m[mid] < test_date:
            low=mid
        else:
            high=mid

event_recommend()