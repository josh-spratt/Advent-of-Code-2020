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
        if birth_year in dict and issue_year in dict and expiration_year in dict and height in dict and hair_color in dict and eye_color in dict and passport_id in dict:
            valid_passport_count = valid_passport_count + 1
        else:
            invalid_passport_count = invalid_passport_count + 1
    return valid_passport_count, invalid_passport_count


puzzle_list = split_puzzle_input_at_double_newlines('puzzle_input.txt')
list_of_dicts = write_puzzle_data_to_list_of_dicts(puzzle_list)
print(check_each_dict_for_required_keys(list_of_dicts))
