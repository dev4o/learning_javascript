function swim(input) {
    let currRecord = Number(input[0])
    let distanceMeters = Number(input[1])
    let meterSwimOneSec = Number(input[2])

    let toSwim = distanceMeters * meterSwimOneSec
    let addTime = Math.floor(distanceMeters / 15) * 12.5
    let totalTime = (toSwim + addTime)

    if (totalTime < currRecord) {
        console.log(`Yes, he succeeded! The new world record is ${(totalTime).toFixed(2)} seconds.`)
    } else {
        console.log(`No, he failed! He was ${(totalTime - currRecord).toFixed(2)} seconds slower.`)
    }
}

swim(["10464",
"1500",
"20"])