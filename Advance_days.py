day = 4
match day:
    case 1 |2|3|4|5:
        print("WeekDays")
    case 6|7:
        print("Weekend")
    case _:
        print("Invalid Input")
