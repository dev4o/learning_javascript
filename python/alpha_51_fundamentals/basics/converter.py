from math import floor

m = int(input()) # miles

one_gallon = 4.54 # liters
one_mile = 1.6 # kms

km_per_liter = (m * one_mile) / one_gallon
print(f"{floor(100 / km_per_liter)} litres per 100 km")
