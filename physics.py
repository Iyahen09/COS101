# STUDENT 2 - PHYSICS CALCULATOR

def density():
    mass = float(input("Enter mass: "))
    volume = float(input("Enter volume: "))
    if volume > 0:
        print("Density =", mass / volume, "kg/m3")
    else:
        print("Volume must be greater than zero")

def momentum():
    mass = float(input("Enter mass: "))
    velocity = float(input("Enter velocity: "))
    print("Momentum =", mass * velocity, "kg m/s")

def pressure():
    force = float(input("Enter force: "))
    area = float(input("Enter area: "))
    if area > 0:
        print("Pressure =", force / area, "Pascals")
    else:
        print("Area must be greater than zero")

def kinetic_energy():
    mass = float(input("Enter mass: "))
    velocity = float(input("Enter velocity: "))
    result = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", result, "Joules")

def potential_energy():
    mass = float(input("Enter mass: "))
    gravity = float(input("Enter gravity: "))
    height = float(input("Enter height: "))
    print("Potential Energy =", mass * gravity * height, "Joules")

while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Density")
    print("2. Momentum")
    print("3. Pressure")
    print("4. Kinetic Energy")
    print("5. Potential Energy")

    option = input("Choose an operation (1-5): ")

    if option == "1":
        density()
    elif option == "2":
        momentum()
    elif option == "3":
        pressure()
    elif option == "4":
        kinetic_energy()
    elif option == "5":
        potential_energy()
    else:
        print("Invalid selection")

    answer = input("Would you like to calculate again? (yes/no): ")
    if answer.lower() != "yes":
        print("Program closed.")
        break
