def open_txt_file_and_read_lines(txt_file):
    with open(txt_file) as f:
        for line in f:
            print(line)


open_txt_file_and_read_lines('pattern.txt')
