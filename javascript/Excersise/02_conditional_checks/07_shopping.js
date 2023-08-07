function shopping(input) {
    let videoPrice = 250
    let final = 0

    let budget = Number(input[0])
    let videoCount = Number(input[1])
    let procCount = Number(input[2])
    let ramCount = Number(input[3])

    let totalVideo = videoPrice * videoCount
    let procPrice = totalVideo * 0.35
    let ramPrice = totalVideo * 0.10
    let totalProc = procPrice * procCount
    let totalRam = ramPrice * ramCount

    let total = totalVideo + totalProc + totalRam

    if (videoCount > procCount) {
        total = total * 0.85
    }
    
    if (budget >= total) {
        final = budget - total
        console.log(`You have ${(final).toFixed(2)} leva left!`)
    } else {
        final = total - budget
        console.log(`Not enough money! You need ${(final).toFixed(2)} leva more!`)
    }
}
shopping(["900",
"2",
"1",
"3"])