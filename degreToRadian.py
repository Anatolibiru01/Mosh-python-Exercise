def degre_to_radian():
    angle = int(input("Enter the angle degre measure: "))
    return f"Degre: {angle} \nRadian: {angle * (3.14/180)}"


print(degre_to_radian())
def circumference(pie_diameter):
    pi = 3.14
    pie_radius = pie_diameter / 2
    circumferences = 2 * pi * pie_radius
    return f"Jimmys pie has a circumference:{circumferences}"


print(circumference(55.4))