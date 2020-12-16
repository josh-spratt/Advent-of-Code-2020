def get_unique_answers(response):
    questions = []  # create a new list called questions
    for char in response:  # for character in the currentResponse
        if char not in questions:  # if the character is not in the questions list
            questions.append(char)  # append the character to the list
    return len(questions)  # return the length of the questions list


with open('puzzle_input.txt', 'r') as f:
    puzzle_input_list = f.readlines()
    puzzle_input_list = [item.strip() for item in
                         puzzle_input_list]  # load the puzzle data into a python list and strip the newline chars

sum = 0
currentResponse = ''
for item in puzzle_input_list:  # for each item in the customs list
    if item != '':  # if the item isn't an empty string
        currentResponse += item  # add that item to the currentResponse string
    else:
        sum += get_unique_answers(currentResponse)
        currentResponse = ''

sum += get_unique_answers(currentResponse)


# part 2
def get_unique_answer_all(responses):
    questions = []
    for char in responses[0]:
        in_all_lines = True
        for line in responses:
            if char not in line:
                in_all_lines = False
        if in_all_lines and char not in questions:
            questions.append(char)
    return len(questions)



sum = 0
currentResponse = []
for item in puzzle_input_list:
    if item != '':
        currentResponse.append(item)
    else:
        sum += get_unique_answer_all(currentResponse)
        currentResponse = []

sum += get_unique_answer_all(currentResponse)
print(sum)