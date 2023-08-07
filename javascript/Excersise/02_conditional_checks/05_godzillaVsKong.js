function gvsk(input) {
    let budget = Number(input[0])
    let ppl = Number(input[1])
    let clothesPrice = Number(input[2])

    let decor = budget * 0.10
    let totalClothes = clothesPrice * ppl

    if (ppl > 150) {
        totalClothes = totalClothes * 0.90
    }

    let totalExepense = decor + totalClothes

    if (budget >= totalExepense) {
        console.log(`Action!`)
        console.log(`Wingard starts filming with ${(budget - totalExepense).toFixed(2)} leva left.`)
    } else {
        console.log(`Not enough money!`)
        console.log(`Wingard needs ${(totalExepense - budget).toFixed(2)} leva more.`)
    }
}

gvsk(["9587.88",
"222",
"55.68"])



