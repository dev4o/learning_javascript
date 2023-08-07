function yardGreening(input) {
    let squareMeterPrice = 7.61
    let yard = input[0]
    let noDisc = yard * squareMeterPrice
    let sum = yard * squareMeterPrice * 0.82
    let disc = noDisc - sum
    console.log(`The final price is: ${sum.toFixed(2)} lv.`)
    console.log(`The discount is: ${disc.toFixed(2)} lv.`)
}

yardGreening(["150"])