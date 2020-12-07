import re

file_regex = re.compile(r"(?:\r?\n){2,}")

input_file = file_regex.split(open('input_file.txt', 'r').read())

passport_valid_regex = re.compile(r"\b((ecl:())|(pid:)|(hcl:)|(eyr:)|(byr:)|(iyr:)|(hgt:))", re.MULTILINE)
passport_present_regex = re.compile(r"\b((ecl:(?:amb|blu|brn|gry|grn|hzl|oth))|(pid:(?:\d{9}\b))|(hcl:(?:#[\dA-Fa-f]{6}))|(eyr:20(?:[2-3]0|2\d))|(byr:(?:19[2-9][\d]|200[0-2]))|(iyr:20(?:[1-2]0|1\d))|(hgt:(?:(?:1(?:[5-8]\d|9[0-3])cm)|(?:(?:59|6\d|7[0-6])in))))", re.MULTILINE)

valid_real = [ passport for passport in input_file if len(passport_valid_regex.findall(passport)) >= 7 ]

present_passports = [ passport for passport in valid_real if len(passport_present_regex.findall(passport)) >= 7 ]

print("Amount of valid passports in input_file: {lenValid}".format(lenValid = len(valid_real)))
print("Amount of resent passports in input_file: {lenPresent}".format(lenPresent = len(present_passports)))
