test_dict = {'range': [2, 5], 'letter': 'c', 'password': 'ccspwpc'}

count = 0
for i in test_dict['password']:
    if i == test_dict['letter']:
        count = count + 1
print(count)
if count <= test_dict['range'][1] and count >= test_dict['range'][0]:
    print('password is valid')
if count > test_dict['range'][1] or count < test_dict['range'][0]:
    print('password is not valid')
