"""
Author: Ryan Warrick
Group: OSUSVT
File: Main.py
Description: The Vehicle Simulator Program for strategy purposes intended to be used by the OSUSVT.
Github Repo: https://github.com/ryanwarrick/VehicleSimulator
"""

__author__ = 'Ryan'

import math

import formulas



# Basic settings/configs for the chart.
data_point_amount = 50
row_length = 63
time_interval = 5  # In minutes

# Constant values of car
watt_hours_of_battery = 4000

# Positions for all columns in chart
index_position = 1
time_position = 7
elevation_position = 12
velocity_position = 22
energy_loss_position = 31
watt_hours_position = 43
state_of_charge_position = 54


# necessary basic variables
template_string = ''
chart_border = '|'  # Used to frame in the chart.
row_string_list = []  # List that holds all strings that make up chart. Will eventually be what is printed to screen.
data_point_list = []  # List of all data_point objects


class Vehicle:
    def __init__(self, e, s):
        self.elevation = e
        self.state_of_charge = s


'''
The class that will create objects to hold each set of data in the chart.
'''


class DataPoint:
    def __init__(self, v, i, t, v2, e, w):  # Takes an argument for each column in the chart.
        self.vehicle = v
        self.index = i
        self.time = t
        self.velocity = v2
        self.elevation = e
        self.watt_hours = w

        self.state_of_charge = (self.watt_hours / watt_hours_of_battery) * 100

        self.theta = 0  # TODO change this so it finds difference from last point to current point in list

        self.power_loss = round((formulas.aero_drag_power_loss(self.velocity) +
                                 formulas.grading_power_loss(self.velocity, self.theta) +
                                 formulas.rolling_resistance_power_loss(self.velocity, self.theta)), 1)

        self.energy_loss = self.power_loss * (time_interval / 60)

    def get_string_output(self):
        return inject_string(template_string,
                             [[chart_border, 0], [str(self.index), index_position],
                              [str(self.time), time_position],
                              [str(self.velocity), velocity_position],
                              [str(self.elevation), elevation_position],
                              [str(round(self.energy_loss, 2)), energy_loss_position],
                              [str(self.watt_hours), watt_hours_position],
                              [str(self.state_of_charge) + '%', state_of_charge_position],
                              [chart_border, row_length - 1]])

    def update_state_of_charge(self):
        self.state_of_charge = round((self.watt_hours / watt_hours_of_battery) * 100, 2)


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
    e = ['Elevation', elevation_position]
    p = ['Energy Loss', energy_loss_position]
    w = ['Watt Hours', watt_hours_position]
    s = ['SOC', state_of_charge_position]
    left_line_border = ['|', 0]
    right_line_border = ['|', row_length - 1]
    key_row_string = inject_string(template_string, [left_line_border, i, t, e, v, p, w, s, right_line_border])
    return key_row_string


# End of Functions
# Beginning of Main Section

print("OSUSVT Vehicle Simulator")  # Prints title of program

phoenix = Vehicle(0, 100)

# Gives template_string correct length
for x in range(row_length):
    template_string += ' '

# Creates data point objects and puts them in list.
for x in range(data_point_amount):
    index = x + 1  # index
    time = x * 5  # time in five minute intervals
    velocity = round(((1 / 2) * (40 - 40 * math.cos(time / 10))), 2)  # sine graph
    # velocity = 10 # Constant 20 mph
    # velocity = x  # Constantly increasingly line
    elevation = 0  # elevation
    watt_hours = watt_hours_of_battery  # Watt hours of car

    dp = DataPoint(phoenix, index, time, velocity, elevation, watt_hours)

    data_point_list.append(dp)  # add new data point with values from above to data point list

for x in range(len(data_point_list)):
    if x > 0:
        data_point_list[x].watt_hours = round(data_point_list[x - 1].watt_hours - data_point_list[x].energy_loss, 2)
        data_point_list[x].update_state_of_charge()


# Does the actual printing of the output.
print(cap_row())
print(get_key_row())
for data_point in data_point_list:
    print(data_point.get_string_output())
print(cap_row())

'''
Notes to self
Power = Force * Velocity
Energy = Power * Time
4kWH battery in car
'''
