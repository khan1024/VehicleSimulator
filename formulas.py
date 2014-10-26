'''
Formulas Module
Contains the functions to perform the necessary grading, rolling resistance and aerodynamics calculations.
Calculates the total power loss the car experiences from these sources.
'''

__author__ = 'Ryan'

import math

# TODO Make sure all values I got off the slides are up to date and accurate.

'''
Power Drain: Grading
Pgrading=m*g*sin(theta)*v

Pgrading= power lost in watts
g = 9.81 m/s^2
v = velocity in m/s
theta = angle of incline in degrees
'''


def grading_power_loss(velocity, theta):
    gravity = 9.81  # m/s^2
    mass = 300  # kg

    # calculate
    power_loss = mass * gravity * math.sin(math.radians(theta)) * velocity

    # return power_loss
    return power_loss


'''
Power Drain: Rolling Resistance
Prr = W*Fr*M*G*Cos(theta)*V
g = 9.81 m/s^2
v = velocity in m/s
m = mass of car in kg = 300
theta = angle of incline in degrees
Prr = power lost in rolling resistance in watts
w = number of wheels
Fr = 0.005
'''

# TODO Figure out if I should specify 4 wheels and then a quarter of the weight or just '1 wheel' and the total weight
def rolling_resistance_power_loss(velocity, theta):
    gravity = 9.81  # m/s^2
    mass = 300  # kg
    # number_of_wheels = 4  # wheels
    friction_coeff = 0.005  # coefficient of friction

    # calculate
    # power_loss = number_of_wheels*friction_coeff*mass*gravity*math.cos(math.radians(theta))*velocity
    power_loss = friction_coeff * mass * gravity * math.cos(math.radians(theta)) * velocity

    # return power_lost
    return power_loss


'''
Power Drain: Aerodynamics
Paero = (1/2)p*Ac*Cd*v^3

Paero = power of drag in watts
p = density of air = ~1.2 kg/m^3
Ac = cross sectional area in m^2 = 0.75
Cd = coefficient of drag = 0.22
    CONSTANT: P(drag) = KV^3
v = velocity in m/s
'''


def aero_drag_power_loss(velocity):
    air_density = 1.2  # kg/m^3
    cross_sectional_area = 0.75  # m^2
    drag_coeff = 0.22

    # calculate
    power_loss = (1 / 2) * air_density * cross_sectional_area * drag_coeff * (velocity ** 3)

    # return power loss
    return power_loss