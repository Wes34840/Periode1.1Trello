Day = input("What day is it today? answer in all caps. ")

if str(Day) == "MONDAY":
    print("get up at 10 am and get ready for school at 1:45 pm")
elif str(Day) == "TUESDAY":
    print("Get up early and get ready for school")
elif str(Day) == "WEDNESDAY":
    print("Get up early and get ready for school") 
elif str(Day) == "THURSDAY":
    print("Get ready for FLEX lessons")
elif str(Day) == "FRIDAY":
    print("Stay at home and go to work at 5 pm")
elif str(Day) == "SATURDAY":
    print("Stay home and go to work at 1 pm")
elif str(Day) == "SUNDAY":
    print("Stay at home and play videogames the entire day")
else:
    print("That's not a day, enter an actually valid day next time")