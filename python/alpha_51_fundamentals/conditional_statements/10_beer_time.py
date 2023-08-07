time_now = input()

am_or_pm = time_now[-2:]
time = time_now[:-6]
min = time_now[-5:-3]

beer_time = False

if not time.isdigit():
    print('invalid time')
    exit()

if int(time) >= 24:
    print('invalid time')
    exit()

if int(min) >= 60:
    print('invalid time')
    exit()

if am_or_pm == 'PM':
    if 0 < int(time) != 12: beer_time = True
    else: beer_time = False

elif len(time_now) == 8 and am_or_pm == 'AM':
    if 11 < int(time) <= 12: beer_time = True
    else: beer_time = False

elif len(time_now) == 7 and am_or_pm == 'AM':
    if 3 > int(time) <= 9: beer_time = True
    else: beer_time = False

if am_or_pm == 'AM':
    if int(time[0]) == 0 or int(time[0]) == 00: beer_time = True

if am_or_pm == 'PM':
    if int(time[0]) == 0 or int(time[0]) == 00:
        print('invalid time')
        exit()


if beer_time:
    print('beer time')
else:
    print('non-beer time')



# solution from other student
# time = input()
 
# hour = time[-8:-6]
# minutes = time[-5:-3]
# time_designator = time[-2:]
 
# if hour.isdigit() and minutes.isdigit() and time_designator == 'PM':
#     if 1 <= int(hour) < 12 and 0 <= int(minutes) <= 59:
#         print('beer time')
#     elif int(hour) == 12 and 0 <= int(minutes) <= 59:
#         print('non-beer time')
 
# elif hour.isdigit() and minutes.isdigit() and time_designator == 'AM':
#     if ( int(hour) == 12 or int(hour) == 1 or int(hour) == 2 )   and 0 <= int(minutes) <= 59:
#         print('beer time')
#     elif 2 < int(hour) < 12 and 0 <= int(minutes) <= 59:
#         print('non-beer time')
# else:
#     print('invalid time')