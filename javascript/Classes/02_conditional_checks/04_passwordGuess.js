function pwd(input) {
    let thePwd = 's3cr3t!P@ssw0rd'
    let guess = input[0]
    if (guess == thePwd) {
        console.log('Welcome')
    } else {
        console.log('Wrong password!')
    }
}

pwd(["s3cr3t!P@ssw0rd"])