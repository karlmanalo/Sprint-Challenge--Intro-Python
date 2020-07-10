# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle (Base Class)

class Vehicle:
    def __init__(self):
        pass

# GroundVehicle (Child of Vehicle Class, parent of Car and Motorcycle classes)

class GroundVehicle(Vehicle):
    def __init__(self):
        pass

# Car (Child of GroundVehicle)

class Car(GroundVehicle):
    def __init__(self):
        pass

# Motorcycle (Child of GroundVehicle)

class Motorcycle(GroundVehicle):
    def __init__(self):
        pass

# FlightVehicle (Child of Vehicle, Parent of Starship and Airplane)

class FlightVehicle(Vehicle):
    def __init__(self):
        pass

# Airplane (Child of FlightVehicle)

class Airplane(FlightVehicle):
    def __init__(self):
        pass

# Starship (Child of FlightVehicle)

class Starship(FlightVehicle):
    def __init__(self):
        pass