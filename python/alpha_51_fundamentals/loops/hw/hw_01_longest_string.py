food_1 = input()

temp_food = ''
while food_1 != 'END':
    if len(food_1) >= len(temp_food):
        temp_food = food_1
    
    food_1 = input()

print(temp_food)
