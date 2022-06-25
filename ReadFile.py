
import string

f = open('Note.txt', 'r')

number_list = []

for line in f:
    number = ""
    for c in line:
        if c == '*':
            break
        else:
            if c.isdigit():
                number += c
            
            if c == "t":
                break

    if number != "":
        print(number)
        number_list.append(number)

sum = 0
# print(len(number_list))
for number in number_list:
    # print(number)
    sum = sum + int(number)

print('Total amount is = ',sum, 'taka')
