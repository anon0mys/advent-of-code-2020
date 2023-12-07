const inputs = ["1-3 a: abcde",
"1-3 b: cdefg",
"2-9 c: ccccccccc"]

function countValidPasswords(inputs) {
    let validPasswordCount = 0
    // Do the code here
    // Loop over inputs, for each input:
    inputs.forEach(input => {
        // 1. Use split to cut up string into min, max, letter, and password
        const [policy, password] = input.split(": ")
        const [minMax, policyLetter] = policy.split(" ")
        const [min, max] = minMax.split("-")
        // 2a. Count the number of times the letter is in the password
        const characterCount = password.reduce((acc, letter) => {
            if (letter == policyLetter) {
                acc += 1
            }
            return acc
        }, 0)
        // 2b. Check if letter is in password more than min, less than max
        if (characterCount >= min && characterCount <= max) {
            // 3. If yes, increment valid count
            validPasswordCount += 1
        }
    })


    console.log(validPasswordCount)
}