import time

seconds_time = time.time()
current_time = time.ctime()
obj_time = time.gmtime(seconds_time)
month = obj_time.tm_mon

match month:
    case 1:
        month_time = "Jan"
    case 2:
        month_time = "Feb"
    case 3:
        month_time = "Mar"
    case 4:
        month_time = "Apr"
    case 5:
        month_time = "Mai"
    case 6:
        month_time = "Jun"
    case 7:
        month_time = "Jul"
    case 8:
        month_time = "Aug"
    case 9:
        month_time = "Sep"
    case 10:
        month_time = "Oct"
    case 11:
        month_time = "Nov"
    case 12:
        month_time = "Dec"


print("Seconds since January 1, 1970:", f"{seconds_time:,.14}", "or", f"{seconds_time:,.4}" + " in scientific notation")
print (month_time, obj_time.tm_mday, obj_time.tm_year)