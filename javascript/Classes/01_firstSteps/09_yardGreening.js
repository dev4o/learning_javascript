function yardGreening(input) {
    let squareMeterPrice = 7.61
    let yard = input[0]
    let sum = yard * squareMeterPrice * 0.82
    let discount = yard * squareMeterPrice - sum
    console.log(`The final price is: ${sum.toFixed(2)} lv.`)
    console.log(`The discount is: ${discount.toFixed(2)} lv.`)
}

yardGreening(["550"])