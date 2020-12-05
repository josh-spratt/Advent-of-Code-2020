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


def find_two_values_in_list_adding_to_2020(expense_report_list):
    # Loops through list of ints to parse out two values which add together to equal '2020'. Returns those two values in a list
    for a in expense_report_list:
        for b in expense_report_list:
            if a + b == 2020:
                return [a, b]


def find_product_of_two_values_in_list(list_of_two_values):
    # Multiplies together two values in a list.
    return list_of_two_values[0]*list_of_two_values[1]


returned_expense_report_list = convert_csv_column_to_list('expense_report.csv')
list_of_two_values = find_two_values_in_list_adding_to_2020(returned_expense_report_list)
print(find_product_of_two_values_in_list(list_of_two_values))
