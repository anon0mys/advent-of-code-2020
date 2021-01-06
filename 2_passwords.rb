# Inputs respect the format:
# min_occurances-max_occurances letter: password
# Output -> how many passwords are valid
test_lines = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc'
]

rule_function = 'positional'

lines = File.new('inputs/2_passwords.txt', 'r')

def parse_line(rule, letter, password)
    [rule.split('-').map(&:to_i), letter[0], password]
end

def password_valid?(password, letter, rule, rule_function)
    if rule_function == 'positional'
        positions = rule.find_all {|position| password[position - 1] == letter}
        positions.count == 1
    else
        (rule[0]...rule[1]).include?(password.count(letter))
    end
end

valid = lines.reduce(0) do |valid_count, line|
    rule, letter, password = parse_line(*line.split(' '))
    valid_count += 1 if password_valid?(password, letter, rule, rule_function)
    valid_count
end

puts("Valid Passwords: #{valid}")

