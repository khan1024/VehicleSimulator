"""
Author: Ryan Warrick
Group: OSUSVT
File: Main.py
Description: The Vehicle Simulator Program for strategy purposes intended to be used by the OSUSVT.
Github Repo: https://github.com/ryanwarrick/VehicleSimulator
"""
__author__ = 'Ryan'

# Basic settings/configs for the chart.
data_point_amount = 100
row_length = 40

# Positions for all columns in chart
index_position = 1
time_position = 7
velocity_position = 12
power_lost_position = 21
soc_position = 32

# necessary basic variables
template_string = ''
chart_border = '|'  # Used to frame in the chart.
row_string_list = []  # List that holds all strings that make up chart. Will eventually be what is printed to screen.
data_point_list = []  # List of all data_point objects

'''
The class that will create objects to hold each set of data in the chart.
'''


class DataPoint:
    def __init__(self, i, t, v):  # Takes an argument for each column in the chart.
        self.index = i
        self.time = t
        self.velocity = v

        self.stateOfCharge = None  # TODO Implement into object
        # TODO Add other types of data we need to object

    def get_string_output(self):
        return inject_string(template_string,
                             [[chart_border, 0], [str(self.index), index_position],
                              [str(self.time), time_position],
                              [str(self.velocity), velocity_position], [chart_border, row_length - 1]])


'''
Arguments:
    original_string: A string you are working with
    Parameters:
        A list of sublists.
        Each sublist contains the content that is desired to be displayed followed by the desired position.
    Will inject the strings within the sublists into the original string in an "insert" fashion in
    order to not change the length of the original string.
    Output:
        output_string. It will return the original string with the newly injected
        strings position correctly inside of it.
'''


def inject_string(original_string, args):
    output_string = original_string
    for l in args:
        inject_str, position = l
        head_section = output_string[:position]
        tail_section = output_string[position + len(inject_str):]
        output_string = head_section + inject_str + tail_section
        output_string = output_string[:len(original_string)]
    return output_string


'''
Populate row_string_list with X amount of blank strings of Y length.
'''


def add_blank_lines():
    for _ in range(data_point_amount):
        row_string_list.append(template_string)


def cap_row():  # add |||| characters across width of row
    return '|' * row_length


def get_key_row():
    i = ['Index', index_position]
    t = ['Time', time_position]
    v = ['Velocity', velocity_position]
    p = ['Power Lost', power_lost_position]
    s = ['SOC', soc_position]
    left_line_border = ['|', 0]
    right_line_border = ['|', row_length - 1]
    key_row_string = inject_string(template_string, [left_line_border, i, t, v, p, s, right_line_border])
    return key_row_string


def line_index_column():
    output_list = []
    count = 1
    for _ in row_string_list:
        output_list.append([str(count), 0])
        count += 1
    return output_list


# End of Functions
# Beginning of Main Section

print("OSUSVT Vehicle Simulator")  # Prints title of program

# Gives template_string correct length
for x in range(row_length):
    template_string += ' '

# Creates data point objects and puts them in list.
for x in range(data_point_amount):
    index = x  # index
    time = x * 5  # time
    velocity = 20  # velocity
    dp = DataPoint(index, time, velocity)
    data_point_list.append(dp)  # add new data point with values from above to data point list


# Does the actual printing of the output.
print(cap_row())
print(get_key_row())
for data_point in data_point_list:
    print(data_point.get_string_output())
print(cap_row())

'''
Notes to self
Power = Force * Velocity
4kWH battery in car
'''
