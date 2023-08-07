function foodDel(input) {
    let priceChicken = 10.35
    let priceFish = 12.40
    let priceVegan = 8.15
    let delivery = 2.50

    let orderChicken = Number(input[0])
    let orderFish = Number(input[1])
    let orderVegan = Number(input[2])

    let total = orderChicken * priceChicken + orderFish * priceFish + orderVegan * priceVegan 
    let totalPlusDesert = total + total * 0.2
    console.log(totalPlusDesert + delivery)
}


foodDel(["9 ",
"2 ",
"6 "])