def ingest_boarding_pass_file_and_store_as_list(boarding_passes):
    boarding_pass_list = []
    with open(boarding_passes, 'r') as f:
        for line in f:
            line = line.strip()
            boarding_pass_list.append(line)
    return boarding_pass_list


def front_back_rows(boarding_pass_list):
    boarding_passes_dict = {}
    row_range = list(range(0, 128))
    half_row_range = len(row_range)//2
    for boarding_pass in boarding_pass_list:
        boarding_pass_dict = {}
        if boarding_pass[0] == 'F':
            row_range_1 = row_range[:half_row_range]
            half_row_range_1 = len(row_range_1)//2
        if boarding_pass[0] == 'B':
            row_range_1 = row_range[half_row_range:]
            half_row_range_1 = len(row_range_1)//2
        if boarding_pass[1] == 'F':
            row_range_2 = row_range_1[:half_row_range_1]
            half_row_range_2 = len(row_range_2)//2
        if boarding_pass[1] == 'B':
            row_range_2 = row_range_1[half_row_range_1:]
            half_row_range_2 = len(row_range_2)//2
        if boarding_pass[2] == 'F':
            row_range_3 = row_range_2[:half_row_range_2]
            half_row_range_3 = len(row_range_3)//2
        if boarding_pass[2] == 'B':
            row_range_3 = row_range_2[half_row_range_2:]
            half_row_range_3 = len(row_range_3)//2
        if boarding_pass[3] == 'F':
            row_range_4 = row_range_3[:half_row_range_3]
            half_row_range_4 = len(row_range_4)//2
        if boarding_pass[3] == 'B':
            row_range_4 = row_range_3[half_row_range_3:]
            half_row_range_4 = len(row_range_4)//2
        if boarding_pass[4] == 'F':
            row_range_5 = row_range_4[:half_row_range_4]
            half_row_range_5 = len(row_range_5)//2
        if boarding_pass[4] == 'B':
            row_range_5 = row_range_4[half_row_range_4:]
            half_row_range_5 = len(row_range_5)//2
        if boarding_pass[5] == 'F':
            row_range_6 = row_range_5[:half_row_range_5]
            half_row_range_6 = len(row_range_6)//2
        if boarding_pass[5] == 'B':
            row_range_6 = row_range_5[half_row_range_5:]
            half_row_range_6 = len(row_range_6)//2
        if boarding_pass[6] == 'F':
            row_range_7 = row_range_6[:half_row_range_6]
            half_row_range_7 = len(row_range_7)//2
        if boarding_pass[6] == 'B':
            row_range_7 = row_range_6[half_row_range_6:]
            half_row_range_7 = len(row_range_7)//2
        boarding_pass_dict['row'] = row_range_7[0]
        boarding_passes_dict[boarding_pass] = boarding_pass_dict
    return boarding_passes_dict


boarding_pass_list = (ingest_boarding_pass_file_and_store_as_list
('boarding_passes.txt'))
print(front_back_rows(boarding_pass_list))
