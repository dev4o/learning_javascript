# Input
# On the first line, you will receive the month as a string
# On the second line, you will receive the date as a number
# Output
# On the only line of output, print the name of the season in pascal case
# Input
# April
# 6

month = input()
date = int(input())

winter = ['January', 'February', 'March']
spring = ['April', 'May', 'June']
summer = ['July', 'August', 'September']
autumn = ['October', 'November', 'December']

if month in winter:
    season = 'Winter'
elif month in spring:
    season = 'Spring'
elif month in summer:
    season = 'Summer'
elif month in autumn:
    season = 'Autumn'

if (month == 'March') and (date >= 20):
    season = 'Spring'
elif (month == 'June') and (date >= 21):
    season = 'Summer'
elif (month == 'September') and (date >= 22):
    season = 'Autumn'
elif (month == 'December') and (date >= 21):
    season = 'Winter'

print(season)