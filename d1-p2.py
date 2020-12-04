import csv


def convert_csv_column_to_list(csv_data):
    # Receives column of csv data, converts values to ints, writes them to list.
    with open(csv_data, 'r') as expense_report_csv:
        lines = expense_report_csv.readlines()
    expense_report_list = []
    for line in lines:
        data = line.split(',')
        expense_report_list.append(int(data[0]))
    return expense_report_list


def find_three_values_in_list_adding_to_2020(expense_report_list):
    # Loops through list of ints to parse out three values which add together to equal '2020'. Returns those three values in a list
    for a in expense_report_list:
        for b in expense_report_list:
            for c in expense_report_list:
                if a + b + c == 2020:
                    return [a, b, c]


def find_product_of_three_values_in_list(list_of_three_values):
    # Multiplies together three values in a list.
    return list_of_three_values[0]*list_of_three_values[1]*list_of_three_values[2]


returned_expense_report_list = convert_csv_column_to_list('expense_report.csv')
list_of_three_values = find_three_values_in_list_adding_to_2020(returned_expense_report_list)
print(find_product_of_three_values_in_list(list_of_three_values))
