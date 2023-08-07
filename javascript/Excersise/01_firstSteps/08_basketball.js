function basket(input) {
    let annualTax = Number(input[0])
    let priceShoes = annualTax * 0.6 // 219
    let priceClothes = priceShoes * 0.8 // 175.20000000000002
    let priceBall = priceClothes / 4 // 43.800000000000004
    let priceAccessory = priceBall / 5 // 8.760000000000002
    let total = annualTax + priceShoes + priceClothes + priceBall + priceAccessory
    console.log(total)
}

basket(["550"])