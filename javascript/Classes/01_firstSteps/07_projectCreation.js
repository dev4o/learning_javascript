function proj(input) {
    let name = input[0]
    let num = input[1]
    let projDeadline = num * 3
    console.log("The architect " + name + " will need " + projDeadline + " hours to complete " + num + " project/s.")
}

proj(["Sanya", "9 "])