mass = float(input('Enter your weight '))
mass_moon = mass * 0.165

print('Mass on the moon is ' + str(mass_moon))

for i in range(15):
    mass_moon = mass * 0.165
    mass +=1

print(f'Mass on earth = {mass} kg | Mass on the moon =  {mass_moon:.2f} kg')
