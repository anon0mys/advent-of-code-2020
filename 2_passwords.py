# Inputs respect the format:
# min_occurances-max_occurances letter: password
# Output -> how many passwords are valid
test_lines = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc'
]

lines = open('inputs/2_passwords.txt').read().split('\n')
# lines = test_lines

rule_function = 'positional'
# rule_function = 'min_max'
valid = 0


def min_max(password, letter, rule):
    min_occurances, max_occurances = rule
    occurances = password.count(letter)
    return occurances in range(min_occurances, max_occurances + 1)


def positional(password, letter, rule):
    occurances = 0
    for position in rule:
        if password[position - 1] == letter:
            occurances += 1
    return occurances == 1


for line in lines:
    rule, letter, password = line.split(' ')
    letter = letter[0]
    rule = [int(i) for i in rule.split('-')]
    if rule_function == 'positional':
        password_valid = positional(password, letter, rule)
    else:
        password_valid = min_max(password, letter, rule)

    if password_valid:
        valid += 1

print(f'Valid Passwords: {valid}')
