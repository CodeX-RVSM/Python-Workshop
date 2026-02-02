mon=10
day =7
match day:
    case 1|2|3|4|5 if mon==1:
        print("WeekDays in jan")
    case 6|7 if mon==10:
        print("Weekend in Feb")
    case _:
        print("Invalid Input")