'''
Author: Ryan Warrick
Group: OSUSVT
File: Main.py
Description: The Vehicle Simulator Program for strategy purposes intended to be used by the OSUSVT.
Github Repo: https://github.com/ryanwarrick/VehicleSimulator
'''
__author__ = 'Ryan'


# def replace_specific_section_of_string(original_string, inject_string, position):
# head_section = original_string[:position]
#     tail_section = original_string[position + len(inject_string):]
#     output_string = head_section + inject_string + tail_section
#     return output_string

def replace_specific_section_of_string(original_string, *args):
    output_string = original_string
    for a in args:
        inject_string = a[0]
        position = a[1]
        head_section = output_string[:position]
        tail_section = output_string[position + len(inject_string):]
        output_string = head_section + inject_string + tail_section
        output_string = output_string[:len(original_string)]
    return output_string

# Power = Force * Velocity
# 4kWH battery in car

template_string = ''

for x in range(30):
    template_string += ' '

print(template_string, '!')

test = ['pewpew', 3]
test2 = ['scrub a dub', 11]
test3 = ['2strong', 28]

header_string = replace_specific_section_of_string(template_string, test, test2)
print(header_string, '!')
second_string = replace_specific_section_of_string(template_string, test3)
print(second_string, '!')

# print("OSUSVT Vehicle Simulator")