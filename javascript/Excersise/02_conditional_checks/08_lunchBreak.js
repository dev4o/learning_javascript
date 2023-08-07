function lunchBreak(input) {
    let seriesName = input[0]
    let episodeLenght = Number(input[1])
    let breakLenght = Number(input[2])

    let rest = breakLenght / 8
    let restTwo = breakLenght / 4
    let totalRest = restTwo + rest

    let freeTime = breakLenght - totalRest

    if (freeTime >= episodeLenght) {
        console.log(`You have enough time to watch ${seriesName} and left with ${Math.ceil(freeTime - episodeLenght)} minutes free time.`)
    } else {
        console.log(`You don't have enough time to watch ${seriesName}, you need ${Math.ceil(episodeLenght - freeTime)} more minutes.`)
    }

}

lunchBreak(["Game of Thrones",
"60",
"96"])

