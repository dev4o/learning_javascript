function animal(input) {
    let what = input[0]
    switch (what) {
        case "dog":
            console.log("mammal"); break;
        case "crocodile":
        case "tortoise":
        case "snake":
            console.log("reptile"); break;
        default:
            console.log("unknown"); break;
    }
}

animal(["cat"])