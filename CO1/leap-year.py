start=int(input("Enter start year: "))
end=int(input("Enter end year: "))
for year in range(start,end):
    if year % 4==0:
        if year%100==0:
            if year%400==0:
                print("{} is a leap year".format(year))
        else:
          print("{} is a leap year".format(year))
