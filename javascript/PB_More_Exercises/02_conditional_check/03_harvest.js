function harvest(input) {
    let land = Number(input[0])
    let grapes = Number(input[1])
    let letersNeeded = Number(input[2])
    let workers = Number(input[3])

    let totalGrapes = grapes * land
    let grapesForWine = (Math.floor(totalGrapes * 0.40) / 2.5)

    if (grapesForWine >= letersNeeded) {
        console.log(`Good harvest this year! Total wine: ${grapesForWine} liters.`)
        console.log(`${grapesForWine - letersNeeded} liters left -> ${((grapesForWine - letersNeeded) / workers)} liters per person.`)
    } else {
        console.log(`It will be a tough winter! More ${Math.floor(letersNeeded - grapesForWine)} liters wine needed.`)
    }

}

harvest(["650","2","175","3"])

// 77/100 judge??