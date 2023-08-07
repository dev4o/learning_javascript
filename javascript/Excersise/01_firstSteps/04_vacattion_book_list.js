function vac_list(input) {
    let pages = Number(input[0])
    let pagesPerHour = Number(input[1])
    let days = Number(input[2])
    let timeForBook = pages / pagesPerHour
    let total = timeForBook / days
    console.log(total)
}

vac_list(["432 ",
"15 ",
"4 "])