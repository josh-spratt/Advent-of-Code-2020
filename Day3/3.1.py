def parse_indexed_values_from_txt_file(txt_file):
    index_value = -3
    new_string = ''
    with open(txt_file) as f:
        for line in f:
            pattern_data = line.replace('\n', '')
            index_value = index_value + 3
            while index_value > 30:
                index_value = index_value - len(pattern_data)
                if index_value <= 30:
                    break
            new_string += pattern_data[index_value]
    print(new_string.count('#'))


parse_indexed_values_from_txt_file('pattern.txt')
