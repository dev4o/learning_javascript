function sleepyCat(input) {
    let daysOff = Number(input[0])
    let workingDays = 365 - daysOff
    let tomSleep = 30000

    let playWorking = workingDays * 63
    let playDaysOff = daysOff * 127
    
    let totalPet = playWorking + playDaysOff
    
    if (tomSleep > totalPet) {
        total = tomSleep - totalPet
    } else {
        total = totalPet - tomSleep
    }

    let hoursPlay = Math.floor(total / 60)
    let minutesLeft = (total % 60)

    if (tomSleep < totalPet) {
        console.log(`Tom will run away`)
        console.log(`${hoursPlay} hours and ${minutesLeft} minutes more for play`)
    } else {
        console.log(`Tom sleeps well`)
        console.log(`${hoursPlay} hours and ${minutesLeft} minutes less for play`)
    }
}

sleepyCat(["113"])
