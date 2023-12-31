function areas(input) {
    let figure = input[0]
    let area = 0
    if (figure === "square") {
        let side = Number(input[1])
        area = side * side;
    } else if(figure === "rectangle") {
        let sideA = Number(input[1])
        let sideB = Number(input[2])
        area = sideA * sideB;
    } else if(figure === "circle") {
        let p = Math.PI
        let r = Number(input[1])
        area = (r * r) * p
    } else if(figure === "triangle") {
        let sideA = Number(input[1])
        let sideB = Number(input[2])
        area = (sideA * sideB) / 2
    }
    console.log(area.toFixed(3))
}

areas(["triangle",
"4.5",
"20"])