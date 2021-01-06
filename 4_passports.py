# The automatic passport scanners are slow because they're having trouble detecting 
# which passports have all required fields. The expected fields are as follows:

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#   If cm, the number must be at least 150 and at most 193.
#   If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def enum_validator(item, elements):
    return item in elements


def year_validator(item, year_range):
    return int(item) in year_range


def height_validator(height, cm_range, in_range):
    unit = height[-2:]
    value = int(height[:-2])
    elements = cm_range if unit == 'cm' else in_range
    return enum_validator(value, elements)


def string_validator(string, length=None, pattern=None):
    is_valid = False
    if length:
        is_valid = len(string) == length
    if pattern:
        valid_prefix = string[0] == pattern['prefix']
        invalid_chars = [char for char in string[1:] if char not in pattern['allowed_chars']]
        is_valid = valid_prefix and not any(invalid_chars)
    return is_valid


required_fields = {
    'byr': {'validator': year_validator, 'criteria': {'year_range': range(1920, 2003)}},
    'iyr': {'validator': year_validator, 'criteria': {'year_range': range(2010, 2021)}},
    'eyr': {'validator': year_validator, 'criteria': {'year_range': range(2020, 2031)}},
    'hgt': {'validator': height_validator, 'criteria': {'cm_range': range(150, 194), 'in_range': range(59, 77)}},
    'hcl': {
        'validator': string_validator,
        'criteria': {
            'length': 7,
            'pattern': {
                'prefix': '#',
                'allowed_chars': '0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f'
            }
        }
    },
    'ecl': {'validator': enum_validator, 'criteria': {'elements': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']}},
    'pid': {'validator': string_validator, 'criteria': {'length': 9}}
}


def validate_passport(passport):
    for field in required_fields:
        try:
            validator = required_fields[field]['validator']
            criteria = required_fields[field]['criteria']
            is_valid = validator(passport[field], **criteria)
            if not is_valid:
                return False
        except KeyError:
            return False
    return True


def update_passport(passport, items):
    for item in items:
        k, v = item.split(':')
        passport[k] = v
    return passport


def check_batch_file(file_name):
    valid_passports = 0
    passport = {}
    with open(file_name, 'r') as batch_file:
        for line in batch_file:
            if line == '\n':
                if validate_passport(passport):
                    valid_passports += 1
                passport = {}
            else:
                items = line.strip().split(' ')
                passport = update_passport(passport, items)
    return valid_passports


valid = check_batch_file('./passports.txt')
print(f'Valid Passports: {valid}')