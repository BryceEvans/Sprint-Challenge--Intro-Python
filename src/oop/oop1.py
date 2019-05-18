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

# Bass Class
class Vehicle:
    pass

# Vehicle --> FlightVehicle
class flightVehicle(Vehicle):
    pass

# Vehicle --> flightVehicle --> Ariplane
class Airplaine(FlightVehicle):
    pass

# Vehicle --> flightVehicle --> Starship
class Starship(FlightVehicle):
    pass


