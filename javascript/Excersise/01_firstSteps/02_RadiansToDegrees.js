function rtod(input) {
    let radians = Number(input[0]);
    let degrees = radians * 180 / Math.PI;
    console.log(degrees);
}

rtod(["6.2832"])