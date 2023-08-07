function shop(input) {
    let product = input[0]
    let city = input[1]
    let howMany = Number(input[2])
    let price = 0

//     if (city === 'Sofia') {
//         if (product === 'coffee') {
//             price = howMany * 0.50
//         } else if (product === 'water') {
//             price = howMany * 0.80
//         } else if (product === 'beer') {
//             price = howMany * 1.20
//         } else if (product == 'sweets') {
//             price = howMany * 1.45
//         } else if (product == 'peanuts') {
//             price = howMany * 1.60
//         }
//     } else if (city === 'Plovdiv') {
//         if (product === 'coffee') {
//             price = howMany * 0.40
//         } else if (product === 'water') {
//             price = howMany * 0.70
//         } else if (product === 'beer') {
//             price = howMany * 1.15
//         } else if (product == 'sweets') {
//             price = howMany * 1.30
//         } else if (product == 'peanuts') {
//             price = howMany * 1.50
//         }        
//     } else if (city === 'Varna')  {
//         if (product === 'coffee') {
//             price = howMany * 0.45
//         } else if (product === 'water') {
//             price = howMany * 0.70
//         } else if (product === 'beer') {
//             price = howMany * 1.10
//         } else if (product == 'sweets') {
//             price = howMany * 1.35
//         } else if (product == 'peanuts') {
//             price = howMany * 1.55
//         }          
//     }
//     console.log(price)
// }


switch (city) {
    case "Sofia":
        switch(product) {
            case "coffee" : price = howMany * 0.50; break;
            case "water" : price = howMany * 0.80; break;
            case "beer" : price = howMany * 1.20; break;
            case "sweets" : price = howMany * 1.45; break;
            case "peanuts" : price = howMany * 1.60; break;
        }
        break;
    case "Plovdiv":
        switch(product) {
            case "coffee" : price = howMany * 0.40; break;
            case "water" : price = howMany * 0.70; break;
            case "beer" : price = howMany * 1.15; break;
            case "sweets" : price = howMany * 1.30; break;
            case "peanuts" : price = howMany * 1.50; break;            
        }
        break;
    case "Varna":
        switch(product) {
            case "coffee" : price = howMany * 0.45; break;
            case "water" : price = howMany * 0.70; break;
            case "beer" : price = howMany * 1.10; break;
            case "sweets" : price = howMany * 1.35; break;
            case "peanuts" : price = howMany * 1.55; break;
        }
        break;
    }
    console.log(price)
}

shop(["beer",
"Sofia",
"2"])
