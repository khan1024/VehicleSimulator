'''
Author: Ryan Warrick
Group: OSUSVT
File: Main.py
Description: The Vehicle Simulator Program for strategy purposes intended to be used by the OSUSVT.
Github Repo: https://github.com/ryanwarrick/VehicleSimulator
'''
__author__ = 'Ryan'

# Power = Force * Velocity
#4kWH battery in car

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

    #return power_loss


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

    #return power loss


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

    #return power_lost


print("OSUSVT Vehicle Simulator")

