#日付の表記 /
Year = int(input())
Month = int(input())
Day = int(input())

rule = Year >=1 and Year <= 2050 and Month >=1 and Month <= 12 and Day >= 1 and Day <=31
if(rule):
    print(Month,end="/")
    print(Day,end="/")
    print(Year)