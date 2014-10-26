__author__ = 'Ryan'

import math

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