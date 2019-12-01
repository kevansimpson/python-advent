import math

def total_required_fuel(masses):
    return sum(list(map(lambda m: required_fuel(m), masses)))

def total_additional_fuel(masses):
    return sum(list(map(lambda m: additional_fuel(m), masses)))

def additional_fuel(mass):
    fuel = required_fuel(mass)
    sum = fuel
    while True:
        next = required_fuel(fuel)
        if next <= 0: return sum
        else:
            sum += next
            fuel = next

def required_fuel(mass):
    return math.floor(mass / 3) - 2
