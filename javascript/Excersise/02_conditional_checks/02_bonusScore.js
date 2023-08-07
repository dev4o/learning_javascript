function bonusScore(input) {
    let x = Number(input[0])
    let y = 0.0
    if (x <= 100) {
        y = 5;
    } else if (x > 100 && x < 1000) {
        y = x - (x * 0.80)
    } else {
        y = x - (x * 0.90)
    }

    if (x % 2 == 0) {
        y += 1;
    } else if (x % 10 == 5) {
        y += 2;
    }
    console.log(y)
    console.log(x + y)
}

bonusScore(["2703"])
