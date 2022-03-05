yr=int(input("enter the year "))
if yr%4==0:
    if yr%100==0:
        if yr%400==0:
            print("{0} is leap year".format(yr))
        else:
            print("{0} not a leap year".format(yr))
    else:
        print("{0} is leap year".format(yr))
else:
    print("{0} not a leap year".format(yr))
