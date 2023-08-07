function paint(input) {
    let item1 = 1.50
    let paint = 14.50
    let paintDiluent = 5

    let item1In = Number(input[0]) + 2
    let paintIn = Number(input[1])
    let paintDiluentIn = Number(input[2])
    let workHours = Number(input[3])

    let addPaint = paintIn * 0.10
    let bags = 0.40
    let allAdd = addPaint + bags

    let total_cost1 = (item1In * item1) 
    let total_cost2 = (paintIn + addPaint) * paint
    let total_cost3 = paintDiluentIn * paintDiluent
    let tot = total_cost1 + total_cost2 + total_cost3 + 0.40
    let painterPay = (tot * 0.3) * workHours
    console.log(painterPay + tot)
}

paint(["5 ",
"10 ",
"10 ",
"1 "])