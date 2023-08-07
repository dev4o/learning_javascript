function pipe(input) {
    let mass = Number(input[0])
    let p1 = Number(input[1])
    let p2 = Number(input[2])
    let hours = Number(input[3])

    let pipe1Usage = p1 * hours // 300
    let pipe2Usage = p2 * hours // 360

    let totalWater = pipe1Usage + pipe2Usage // 660

    let pipe1Final = ((pipe1Usage / totalWater) * 100).toFixed(2) // 45.45
    let pipe2Final = ((pipe2Usage / totalWater) * 100).toFixed(2) // 54.55

    let totalPool = ((totalWater / mass) * 100).toFixed(2) // 66.00

    if (totalWater <= mass) {
        console.log(`The pool is ${totalPool}% full. Pipe 1: ${pipe1Final}%. Pipe 2: ${pipe2Final}%.`)
    } else {
        console.log(`For ${(hours).toFixed(2)} hours the pool overflows with ${(totalWater - mass).toFixed(2)} liters.`)
    }
}

pipe(["100","100","100","2.5"])