def parse_indexed_nth_values_from_txt_file(txt_file, n_value):
    n = n_value
    index_value = -n
    new_string = ''
    with open(txt_file) as f:
        for line in f:
            pattern_data = line.replace('\n', '')
            index_value = index_value + n
            while index_value > 30:
                index_value = index_value - len(pattern_data)
                if index_value <= 30:
                    break
            new_string += pattern_data[index_value]
    return int(new_string.count('#'))


def right_one_down_two_slope(txt_file, n_value):
    n = n_value
    index_value = -n
    new_string = ''
    with open(txt_file) as f:
        for count, line in enumerate(f, start=0):
            if count % 2 == 0:
                line = line
                pattern_data = line.replace('\n', '')
                index_value = index_value + n
                while index_value > 30:
                    index_value = index_value - len(pattern_data)
                    if index_value <= 30:
                        break
                new_string += pattern_data[index_value]
    return int(new_string.count('#'))


a = parse_indexed_nth_values_from_txt_file('pattern.txt',1)
b = parse_indexed_nth_values_from_txt_file('pattern.txt',3)
c = parse_indexed_nth_values_from_txt_file('pattern.txt',5)
d = parse_indexed_nth_values_from_txt_file('pattern.txt',7)
e = right_one_down_two_slope('pattern.txt', 1)

print(a*b*c*d*e)
