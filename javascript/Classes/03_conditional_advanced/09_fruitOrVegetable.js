function forv(input) {
    let item = input[0]
    let what = ''
    switch (item) {
        case 'banana' : what = 'fruit'; break;
        case 'apple' : what = 'fruit'; break;
        case 'kiwi' : what = 'fruit'; break;
        case 'cherry' : what = 'fruit'; break;
        case 'lemon' : what = 'fruit'; break;
        case 'grapes' : what = 'fruit'; break;
        case 'tomato' : what = 'vegetable'; break;
        case 'cucumber' : what = 'vegetable'; break;
        case 'pepper' : what = 'vegetable'; break;
        case 'carrot' : what = 'vegetable'; break;
    default:
        console.log('unknown')

    }
    console.log(what)
}

forv(["apple"])