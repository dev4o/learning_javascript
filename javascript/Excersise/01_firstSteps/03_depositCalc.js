function dcalc(input) {
    let deposit = Number(input[0]);
    let deposit_time = Number(input[1]);
    let yearly_percent = Number(input[2]) / 100;
    let lihva = deposit * yearly_percent
    let lihva_1month = lihva / 12
    let total = deposit + deposit_time * lihva_1month
    console.log(total)
}

dcalc(["2350",
"6 ",
"7 "])