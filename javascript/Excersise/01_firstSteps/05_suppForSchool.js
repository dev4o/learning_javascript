function supForSchool(input) {
    let pricePens = 5.80
    let priceMarkers = 7.20
    let preparat = 1.20
    let packPens = Number(input[0])
    let packMarkers = Number(input[1])
    let preparatLiters = Number(input[2])
    let dcount = Number(input[3]) / 100
    let totalPens = packPens * pricePens
    let totalMarkers = packMarkers * priceMarkers
    let totalPreparat = preparatLiters * preparat
    let totalTools = totalPens + totalMarkers + totalPreparat
    let totalLast = totalTools - (totalTools * dcount)
    console.log(totalLast)
}

supForSchool(["4 ",
"2 ",
"5 ",
"13 "])