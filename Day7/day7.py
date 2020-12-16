with open('rules_list.txt', 'r') as f:
    raw_input_data = f.readlines()
    input_data = [line.strip() for line in raw_input_data]


def get_number_of_bags(color):
    lines = [line for line in input_data if color in line and line.index(color) != 0]
    all_colors = []
    if len(lines) == 0:
        return []
    else:
        colors = [line[:line.index(' bags')] for line in lines]
        colors = [color for color in colors if color not in all_colors]
        for color in colors:
            all_colors.append(color)
            bags = get_number_of_bags(color)
            all_colors += bags
        unique_colors = []
        for color in all_colors:
            if color not in unique_colors:
                unique_colors.append(color)
        return unique_colors

colors = get_number_of_bags('shiny gold')
print(len(colors))


#part 2


def get_bag_count(color):
    rule = ''
    for line in input_data:
        if line[:line.index(' bags')] == color:
            rule = line
    if 'no' in rule:
        return 1
    rule = rule[rule.index('contain')+8:].split()
    total = 0
    i = 0
    while i < len(rule):
        count = int(rule[i])
        color = rule[i+1] + ' ' + rule[i+2]
        total += count * get_bag_count(color)
        i += 4
    return total + 1


count = get_bag_count('shiny gold')
print(count)
