from collections import OrderedDict
import collections


def parse_input_file_and_create_list(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().rstrip()
        raw_list_of_lines = lines.split('\n\n')
    return raw_list_of_lines


def if_item_contains_newline_split_into_list(raw_list_of_lines):
    customs_list_of_lists = [char.split('\n') for char in raw_list_of_lines]
    return customs_list_of_lists


def check_list_of_lists_for_repetitive_chars(customs_list_of_lists):
    solo_person_count = 0
    list_of_group_declarations = []
    for customs_declaration in customs_list_of_lists:
        if len(customs_declaration) == 1:
            for person in customs_declaration:
                solo_person_count = solo_person_count + len(set(person))
        if len(customs_declaration) > 1:
            group_customs_declaration = str(''.join(customs_declaration))
            list_of_group_declarations.append(group_customs_declaration)
    print('solo person count:', solo_person_count)
    #print('new_list:',list_of_group_declarations)
    return list_of_group_declarations


def calculate_number_for_groups(list_of_group_declarations):
    difference_list = []
    for a in list_of_group_declarations:
        number_of_unique_chars = len(set(a))
        total_number_of_chars = len(a)
        difference = total_number_of_chars - number_of_unique_chars
        difference_list.append(difference)
    print('group count:',sum(difference_list))



raw_list_of_lines = parse_input_file_and_create_list('puzzle_input.txt')
customs_list_of_lists = if_item_contains_newline_split_into_list(raw_list_of_lines)
list_of_group_declarations = check_list_of_lists_for_repetitive_chars(customs_list_of_lists)
calculate_number_for_groups(list_of_group_declarations)