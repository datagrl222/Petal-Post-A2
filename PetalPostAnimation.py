from visual import *

# Canvas parameter
scene = display(title='PetalPost Daisy', width=800, height=800, center=(0, 0, 0))

# Integrate user input for message
message = input("Enter your desired message: ")

# Create a label to display the message (Code for text from LearntoTech tutorial)
text = label(pos=(0, 0.8, 0), text=message, height=40, color=color.yellow)

# Create flowers centre
center = sphere(pos=(0, 0, 0), radius=0.3, color=color.yellow, material=materials.plastic)

# Create the petals
petals = []
for i in range(6):
    petal = sphere(pos=(0.8 * cos(2 * pi * i / 6), 0.8 * sin(2 * pi * i / 6), 0), radius=0.2, color=color.white, material=materials.plastic)
    petals.append(petal)

# Set the maximum petal radius
max_radius = 0.55

# Animate the petals (Inspired by Paul McWhorter's tutorial)
while True:
    rate(50)
    for petal in petals:
        petal.rotate(angle=0.01, axis=(0, 0, 1), pos=center.pos)
        if petal.radius < max_radius:
            petal.radius += 0.001


