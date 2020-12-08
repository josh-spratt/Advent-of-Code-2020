def split_puzzle_input_at_double_newlines(puzzle_input):
    with open(puzzle_input) as f:
        lines = f.read()
        puzzle_list = lines.split('\n\n')
        return puzzle_list


def write_puzzle_data_to_list_of_dicts(puzzle_list):
    resultant_list = []
    for string in puzzle_list:
        string = string.replace('\n', ' ').rstrip()
        passport_dict = dict(item.split(':') for item in string.split(' '))
        resultant_list.append(passport_dict)
    return resultant_list


def check_each_dict_for_required_keys(list_of_dicts):
    list_of_valid_passports = []
    valid_passport_count = 0
    invalid_passport_count = 0
    birth_year = 'byr'
    issue_year = 'iyr'
    expiration_year = 'eyr'
    height = 'hgt'
    hair_color = 'hcl'
    eye_color = 'ecl'
    passport_id = 'pid'
    country_id = 'cid'
    for dict in list_of_dicts:
        if (birth_year in dict and issue_year in dict and expiration_year in
        dict and height in dict and hair_color in dict and eye_color in dict
        and passport_id in dict):
            valid_passport_count = valid_passport_count + 1
            list_of_valid_passports.append(dict)
        else:
            invalid_passport_count = invalid_passport_count + 1
    return list_of_valid_passports


def check_valid_passports_byr_iyr_eyr(valid_passports):
    byr_iyr_eyr_checked_list = []
    for passport in valid_passports:
        if (len(passport['byr']) == 4 and passport['byr'] >= '1920' and
        passport['byr'] <= '2002' and len(passport['iyr']) == 4 and
        passport['iyr'] >= '2010' and passport['iyr'] <= '2020' and
        len(passport['eyr']) == 4 and passport['eyr'] >= '2020' and
        passport['eyr'] <= '2030'):
            byr_iyr_eyr_checked_list.append(passport)
    return byr_iyr_eyr_checked_list


def check_valid_passports_hgt(valid_passports):
    initial_hgt_checked_list = []
    for passport in valid_passports:
        if 'cm' or 'in' in passport['hgt']:
            initial_hgt_checked_list.append(passport)
    final_hgt_checked_list = []
    for passport in initial_hgt_checked_list:
        if 'cm' in passport['hgt']:
            passport['hgt'] = passport['hgt'].replace('cm','')
            if passport['hgt'] >= '150' and passport['hgt'] <= '193':
                final_hgt_checked_list.append(passport)
        if 'in' in passport['hgt']:
            passport['hgt'] = passport['hgt'].replace('in','')
            if passport['hgt'] >= '59' and passport['hgt'] <= '76':
                final_hgt_checked_list.append(passport)
    return final_hgt_checked_list


def check_valid_passports_hcl_ecl(final_hgt_checked_list):
    hcl_checked_list = []
    for passport in final_hgt_checked_list:
        if passport['hcl'][0] == '#':
            hcl_checked_list.append(passport)
    ecl_checked_list = []
    for passport in hcl_checked_list:
        if (passport['ecl'] == 'amb' or passport['ecl'] == 'blu' or
        passport['ecl'] == 'brn' or passport['ecl'] == 'gry' or passport['ecl']
        == 'grn' or passport['ecl'] == 'hzl' or passport['ecl'] == 'oth'):
            ecl_checked_list.append(passport)
    pid_checked_list = []
    for passport in ecl_checked_list:
        if len(passport['pid']) == 9:
            pid_checked_list.append(passport)
    return pid_checked_list


puzzle_list = split_puzzle_input_at_double_newlines('puzzle_input.txt')
list_of_dicts = write_puzzle_data_to_list_of_dicts(puzzle_list)
x = check_each_dict_for_required_keys(list_of_dicts)
y = check_valid_passports_byr_iyr_eyr(x)
z = check_valid_passports_hgt(y)
zz = check_valid_passports_hcl_ecl(z)
print(len(zz))
