#Constants Gravity 
MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
URANUS = 0.92
NEPTUNE = 1.12
PLUTO = 0.066

#User Input
name = input("What is your name: ")
weight = float(input("What is your weight: "))

weightMercury = weight * MERCURY
weightVenus = weight * VENUS
weightMoon = weight * MOON
weightMars = weight * MARS
weightJupiter = weight * JUPITER
weightSaturn = weight * SATURN
weightUranus = weight * URANUS
weightNeptune = weight * NEPTUNE
weightPluto = weight * PLUTO

#output
print(name + " here are your weights on our Solar System's planets:")
print("Weight on Mercury:           " + str(format(weightMercury,',.2f')))
print("Weight on Venus:             " + str(format(weightVenus,',.2f')))
print("Weight on our Moon:          " + str(format(weightMoon,',.2f')))
print("Weight on Mars:              " + str(format(weightMars,',.2f')))
print("Weight on Jupiter:           " + str(format(weightJupiter,',.2f')))
print("Weight on Saturn:            " + str(format(weightSaturn,',.2f')))
print("Weight on Uranus:            " + str(format(weightUranus,',.2f')))
print("Weight on Neptune:           " + str(format(weightNeptune,',.2f')))
print("Weight on Pluto:             " + str(format(weightPluto,',.2f')))
