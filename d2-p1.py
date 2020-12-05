

def open_txt_file_and_read_lines_to_list_of_dicts(txt_file):
    list_of_dicts_to_return = []
    with open(txt_file) as f:
        for line in f:
            d = {}
            d['range'] = [int(i) for i in line.split()[0].split('-')]
            d['letter'] = line.split()[1].replace(':', '')
            d['password'] = line.split()[2]
            list_of_dicts_to_return.append(d)
    return list_of_dicts_to_return


def count_number_of_occurrences_of_letter_in_password(list_of_dicts):
    valid_passwords = []
    invalid_passwords = []
    for password_dict in list_of_dicts:
        count = 0
        for i in password_dict['password']:
            if i == password_dict['letter']:
                count = count + 1
        if count <= password_dict['range'][1] and count >= password_dict['range'][0]:
            valid_passwords.append('valid')
        if count > password_dict['range'][1] or count < password_dict['range'][0]:
            invalid_passwords.append('invalid')
    print(len(valid_passwords))
    print(len(invalid_passwords))


list_of_dicts = open_txt_file_and_read_lines_to_list_of_dicts(
    'north-pole-toboggan-rental-passwords.txt')
count_number_of_occurrences_of_letter_in_password(list_of_dicts)
