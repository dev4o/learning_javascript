function fishTank(input) {
    let tankLenght = Number(input[0])
    let tankWidth = Number(input[1])
    let tankHeight = Number(input[2])
    let tankPercent = Number(input[3])

    let tankSize = tankLenght * tankWidth * tankHeight / 1000
    let percent = tankPercent / 100
    let total = tankSize * (1 - percent)
    console.log(total)
}

fishTank(["105 ",
"77 ",
"89 ",
"18.5 "])