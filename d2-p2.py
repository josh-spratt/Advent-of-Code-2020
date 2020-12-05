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


def manipulate_list_of_dicts_to_new_output(list_of_dicts):
    manipulated_list = []
    for password_dict in list_of_dicts:
        new_dict = {}
        range_index_1 = password_dict['range'][0] - 1
        range_index_2 = password_dict['range'][1] - 1
        new_dict['letter'] = password_dict['letter']
        new_dict['manipulated_password'] = password_dict['password'][range_index_1] + password_dict['password'][range_index_2]
        manipulated_list.append(new_dict)
    return manipulated_list


def take_manipulated_list_and_check_password_values_to_letter(manipulated_list):
    valid_password_count = 0
    invalid_password_count = 0
    for dict in manipulated_list:
        if dict['manipulated_password'][0] == dict['letter'] and dict['manipulated_password'][1] == dict['letter']:
            invalid_password_count = invalid_password_count + 1
        if dict['manipulated_password'][0] != dict['letter'] and dict['manipulated_password'][1] != dict['letter']:
            invalid_password_count = invalid_password_count + 1
        if dict['manipulated_password'][0] != dict['letter'] and dict['manipulated_password'][1] == dict['letter']:
            valid_password_count = valid_password_count + 1
        if dict['manipulated_password'][0] == dict['letter'] and dict['manipulated_password'][1] != dict['letter']:
            valid_password_count = valid_password_count + 1
    print(valid_password_count)
    print(invalid_password_count)


list_of_dicts = open_txt_file_and_read_lines_to_list_of_dicts(
    'north-pole-toboggan-rental-passwords.txt')
x = manipulate_list_of_dicts_to_new_output(list_of_dicts)
take_manipulated_list_and_check_password_values_to_letter(x)
