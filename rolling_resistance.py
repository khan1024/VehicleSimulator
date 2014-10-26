'''
Rolling Resistance Module
'''

__author__ = 'Ryan'

import math

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