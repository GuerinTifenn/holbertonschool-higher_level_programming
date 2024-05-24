#!/usr/bin/python3
"""Create a mixins"""


# Define the SwimMixin
class SwimMixin:
    def swim(self):
        print("The creature swims!")


# Define the FlyMixin
class FlyMixin:
    def fly(self):
        print("The creature flies!")


# Define the Dragon class inheriting from both SwimMixin and FlyMixin
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
