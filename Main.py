'''
Author: Ryan Warrick
Group: OSUSVT
File: Main.py
Description: The Vehicle Simulator Program for strategy purposes intended to be used by the OSUSVT.
Github Repo: https://github.com/ryanwarrick/VehicleSimulator
'''
__author__ = 'Ryan'

iterations = 100
row_length = 40
template_string = ''


def inject_string(original_string, args):
    count = 0
    output_string = original_string
    for list in args:
        # for sublist in list:
        inject_string = list[0]
        position = list[1]
        head_section = output_string[:position]
        tail_section = output_string[position + len(inject_string):]
        output_string = head_section + inject_string + tail_section
        output_string = output_string[:len(original_string)]
    return output_string


def add_blank_lines(length):
    for x in range(iterations):
        row_string_list.append(template_string)


def line_index_column():
    output_list = []
    count = 1
    for x in row_string_list:
        output_list.append([str(count), 0])
        count += 1
    return output_list


def add_key_row():
    index = ['Index', 0]
    time = ['Time', 6]
    velocity = ['Velocity', 18]
    key_row_string = inject_string(template_string, [index, time, velocity])
    row_string_list.insert(0, key_row_string)


def time_column():
    output_list = []
    time = 0  # minutes
    for x in row_string_list:
        output_list.append([str(time), 6])
        time += 5
    return output_list


def end_line_column():
    output_list = []
    for x in row_string_list:
        output_list.append(['!', row_length - 1])
    return output_list


# Power = Force * Velocity
# 4kWH battery in car

print("OSUSVT Vehicle Simulator")

for x in range(row_length):
    template_string += ' '

row_string_list = []

add_blank_lines(row_length)  #special method that populates row_string_list

index_list = line_index_column()
time_column_list = time_column()
end_line_column_list = end_line_column()

for r in range(len(row_string_list)):
    row_string_list[r] = inject_string(row_string_list[r],
                                       [index_list[r], time_column_list[r], end_line_column_list[r]])

add_key_row()


# output final product
for r in row_string_list:
    print(r)