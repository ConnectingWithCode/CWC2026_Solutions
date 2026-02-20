def from_feet_to_inches(feet):
    return feet * 12

def from_inches_to_feet(inches):
    return inches / 12

def from_inches_to_feet_inches(inches):
    feet = inches // 12
    remaining_inches = inches % 12
    return feet, remaining_inches

def square_feet_to_square_inches(square_feet):
    return square_feet * 12 * 12

def square_inches_to_square_feet(square_inches):
    return square_inches / 12 / 12

# On their own
def from_inches_to_centimeters(inches):
    return inches * 2.54

def from_centimeters_to_inches(centimeters):
    return centimeters / 2.54

# Back together again
def from_f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def from_c_to_f(celsius):
    return (celsius * 9/5) + 32

def main():
    print(from_feet_to_inches(5))
    print(from_inches_to_feet(60))
    print(from_inches_to_feet(62))
    print(from_inches_to_feet_inches(62))
    print(square_feet_to_square_inches(10))
    print(square_inches_to_square_feet(1440))
    print(from_inches_to_centimeters(10))
    print(from_centimeters_to_inches(25.4))
    print(from_f_to_c(100))
    print(from_c_to_f(37))

main()