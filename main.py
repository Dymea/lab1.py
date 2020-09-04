# Author: Dymea Schippers dxs5940@psu.edu
# Collaborator: Tyler Ciuca tmc6093@psu.edu
# Collaborator: Chetan Mitra czm5805@psu.edu
# Collaborator: Jian Hong WOng jpw6087@psu.edu

temp = input("Enter temperature in celsius: ")
unit = input("Enter unit in F/f or C/c: ")

if unit == "C" or unit == "c":
    celsius = float(temp)
    print(f"{celsius}° in Celsius is equivalent to {celsius * 1.8 + 32}° Fahrenheit.")

elif unit == "F" or unit == "f":
  fahrenheit = float(temp)
  print(f"{fahrenheit}° in Fahrenheit is equivalent to {(fahrenheit-32)*5/9}° Celsius.")

else :
  print(f"Invalid unit({unit}).")

