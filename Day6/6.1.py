from collections import OrderedDict
def parse_input_file_and_create_list(input_file):
    with open(input_file, 'r') as f:
        lines = f.read()
        raw_list_of_lines = lines.split('\n\n')
    return raw_list_of_lines


def clean_newlines_and_duplicates_from_list(raw_list_of_lines):
    clean_list_of_lines = []
    for line in raw_list_of_lines:
        line = line.replace('\n', '')
        clean_list_of_lines.append(line)
    removed_duplicates_count_list = []
    for item in clean_list_of_lines:
        item = ''.join(OrderedDict.fromkeys(item))
        removed_duplicates_count_list.append(len(item))
    return removed_duplicates_count_list


raw_list_of_lines = parse_input_file_and_create_list('puzzle_input.txt')

removed_duplicates_count_list = clean_newlines_and_duplicates_from_list(raw_list_of_lines)
customs_declaration_forms_count = sum(removed_duplicates_count_list)
print(customs_declaration_forms_count)
