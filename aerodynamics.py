'''
Aerodynamics Module
'''

__author__ = 'Ryan'

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