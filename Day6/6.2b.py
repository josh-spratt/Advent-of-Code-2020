import collections


def parse_input_file_and_create_list(input_file):
    with open(input_file, 'r') as f:
        lines = f.read()
        raw_list_of_lines = lines.split('\n\n')
    return raw_list_of_lines


def clean_newlines_from_list(raw_list_of_lines):
    solos = []
    groups = []
    for line in raw_list_of_lines:
        rstrip_line = line.rstrip()
        if '\n' in rstrip_line:
            groups.append(rstrip_line)
        elif '\n' not in rstrip_line:
            solos.append(rstrip_line)
    return solos, groups


def getting_groups_counts(groups_list):
    new_groups_list = []
    for a in groups_list:
        a = a.split('\n')
        new_groups_list.append(a)
    list_of_dicts_char_counts = []
    for b in new_groups_list:
        frequencies = collections.Counter(b)
        repeated = {}
        for key, value in frequencies.items():
            if value > 1:
                repeated[key] = value
        list_of_dicts_char_counts.append(repeated)
    print(list_of_dicts_char_counts)


    """groups_list_minus_newlines = []
    list_of_dicts_char_counts = []
    for string in groups_list:
        string = string.replace('\n','')
        groups_list_minus_newlines.append(string)
    for item in groups_list_minus_newlines:
        frequencies = collections.Counter(item)
        repeated = {}
        for key, value in frequencies.items():
            if value > 1:
                repeated[key] = value
        list_of_dicts_char_counts.append(repeated)
    count = 0
    for a in list_of_dicts_char_counts:
        count = count + len(a)
    print(count)"""


def getting_solos_counts(solos_list):
    count = 0
    for item in solos_list:
        count = count + len(item)
    print(count)


raw_list_of_lines = parse_input_file_and_create_list('puzzle_input.txt')
#print(raw_list_of_lines)
solos_list, groups_list = clean_newlines_from_list(raw_list_of_lines)
#print('solos list:', solos_list)
#print('groups list:', groups_list)
getting_groups_counts(groups_list)
#getting_solos_counts(solos_list)