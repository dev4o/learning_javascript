function numRamge(input) {
    let num123 = Number(input[0]);
    if (num123 < 100) {
        console.log("Less than 100") 
    } else if (num123 >= 100 && num123 <= 200) {
        console.log("Between 100 and 200")
    } else {
        console.log("Greater than 200")
    }
}

numRamge(["200"])