# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

def cal(year,month,day):
    print(str(calendar.day_name[calendar.weekday(year, month, day)]).upper())

k=cal(2015,5,8)
