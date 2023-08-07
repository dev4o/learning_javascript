function numInRange(input) {
    let x = Number(input[0])

    if (x <= 100 && x >= -100 && x != 0) {
        console.log('Yes')
    } else {
        console.log('No')
    }
}

numInRange(["1125"])