'''
Rolling Resistance Module
'''

__author__ = 'Ryan'

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


def rolling_resistance_power_loss(velocity, theta):
    gravity = 9.81  # m/s^2
    mass = 300  # kg
    number_of_wheels = 4  # wheels
    friction_coeff = 0.005  # coefficient of friction

    # calculate

    # return power_lost