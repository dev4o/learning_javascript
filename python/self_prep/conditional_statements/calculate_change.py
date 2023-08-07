price = float(input()) * 100 # from leva to stotinki
paid_amount = float(input()) * 100
change = paid_amount - price

if change // 100:
    number = change // 100
    print(f"{number:.0f} x 1 lev")
    change -= number * 100

if change // 50:
    number = change // 50
    print(f"{number:.0f} x 50 stotinki")
    change -= number * 50

if change // 20:
    number = change // 20
    print(f"{number:.0f} x 20 stotinki")
    change -= number * 20

if change // 10:
    number = change // 10
    print(f"{number:.0f} x 10 stotinki")
    change -= number * 10

if change // 5:
    number = change // 5
    print(f"{number:.0f} x 5 stotinki")
    change -= number * 5

if change // 2:
    number = change // 2
    print(f"{number:.0f} x 2 stotinki")
    change -= number * 2

if change // 1:
    number = change // 1
    print(f"{number:.0f} x 1 stotinka")
    change -= number * 1