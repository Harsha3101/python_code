# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

def cal(year,month,day):
    return str(calendar.day_name[calendar.weekday(year, month, day)]).upper()


