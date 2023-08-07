txt_mes_total = int(input())
min_total = int(input())

add_mes = 0
add_min = 0
add_mes_cost = 0
add_min_cost = 0
tax = 0

#if txt_mes_total <= 20 and min_total <= 60:
#    initial_sum = 12
if txt_mes_total > 20:
    add_mes = txt_mes_total - 20
    add_mes_cost = add_mes * 0.06
if min_total > 60:
    add_min = min_total - 60 
    add_min_cost = add_min * 0.1
    
tax = (add_mes_cost + add_min_cost) * 0.2

print(f"{add_mes} additional messages for {add_mes_cost:.2f} levas")
print(f"{add_min} additional minutes for {add_min_cost:.2f} levas")
print(f"{tax:.2f} additional taxes")
print(f"{add_mes_cost + add_min_cost + tax + 12:.2f} total bill")