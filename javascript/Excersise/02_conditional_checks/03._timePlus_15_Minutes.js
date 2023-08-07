function time15(input) {
    let hour = Number(input[0])
    let minute = Number(input[1])
    if ((minute + 15) >= 60) {
        minute = (minute + 15) - 60;
        hour += 1
    } else {
        minute += 15
    }

    if (hour == 24) {
        hour = 0
    }

    if (minute == 60) {
        minute = 0
    }

    if (minute < 10) {
        console.log(`${hour}:0${minute}`);
    } else {
        console.log(`${hour}:${minute}`);
    }
}

time15(["0", "01"])