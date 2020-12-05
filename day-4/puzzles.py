import re

with open("input.txt") as f:
    raw_input = f.read()


tokens = re.split("[ \n]", raw_input)


def parse_passport(tokens):
    passport = {}
    while tokens[0]:
        token = tokens.pop(0)
        key, value = token.split(":")
        passport[key] = value
    tokens.pop(0)
    return passport


def parse_passports(tokens):
    passports = []
    while tokens:
        passports.append(parse_passport(tokens))
    return passports


def is_valid_byr(passport):
    if "byr" not in passport:
        return False
    byr = passport["byr"]
    return len(byr) == 4 and byr >= "1920" and byr <= "2002"


def is_valid_iyr(passport):
    if "iyr" not in passport:
        return False
    iyr = passport["iyr"]
    return len(iyr) == 4 and iyr >= "2010" and iyr <= "2020"


def is_valid_eyr(passport):
    if "eyr" not in passport:
        return False
    eyr = passport["eyr"]
    return len(eyr) == 4 and eyr >= "2020" and eyr <= "2030"


def is_valid_hgt(passport):
    if "hgt" not in passport:
        return False

    hgt = passport["hgt"]
    match = re.match(r"(\d{2,3})(\w\w)", hgt)

    if not match:
        return False

    height = match[1]
    unit = match[2]

    if unit not in ["cm", "in"]:
        return False

    if unit == "cm":
        return height >= "150" and height <= "193"
    else:
        return height >= "59" and height <= "76"


def is_valid_hcl(passport):
    if "hcl" not in passport:
        return False

    hcl = passport["hcl"]
    match = re.match(r"^#([a-f]|\d){6}$", hcl)

    if not match:
        return False
    return True


def is_valid_ecl(passport):
    if "ecl" not in passport:
        return False

    ecl = passport["ecl"]
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def is_valid_pid(passport):
    if "pid" not in passport:
        return False

    pid = passport["pid"]
    match = re.match(r"^\d{9}$", pid)

    if not match:
        return False
    return True


VALIDATORS = [
    is_valid_byr,
    is_valid_iyr,
    is_valid_eyr,
    is_valid_hgt,
    is_valid_hcl,
    is_valid_ecl,
    is_valid_pid,
]


def is_valid(passport):
    return all(validator(passport) for validator in VALIDATORS)


passports = parse_passports(tokens)

valid_passports = [passport for passport in passports if is_valid(passport)]

print(len(valid_passports))
