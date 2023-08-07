function toyShop(input) {
    let puzzle = 2.60
    let doll = 3
    let bear = 4.10
    let minion = 8.20
    let truck = 2
    let discount = 0
    let rent = 0

    let tripPrice = Number(input[0])
    let puzzleN = Number(input[1])
    let dollN = Number(input[2])
    let bearN = Number(input[3])
    let minionN = Number(input[4])
    let truckN = Number(input[5])

    let totalToys = puzzleN + dollN + bearN + minionN + truckN
    let totalSum = (puzzleN * puzzle) + (dollN * doll) + (bearN * bear) + (minionN * minion) + (truckN * truck)

    if (totalToys >= 50) {
        totalSum = totalSum * 0.75
    }
    
    totalSum = totalSum * 0.90

    if (totalSum >= tripPrice) {
        console.log(`Yes! ${(totalSum - tripPrice).toFixed(2)} lv left.`)
    } else {
        console.log(`Not enough money! ${(tripPrice - totalSum).toFixed(2)} lv needed.`)
    }
}

toyShop(["320",
"8",
"2",
"5",
"5",
"1"])