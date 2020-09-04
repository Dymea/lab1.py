temp = input("Enter temperature in celsius: ")
unit = input("Enter unit in F/f or C/c: ")

if unit == "F" or unit == "f":
  fahrenheit = float(temp)
  print(f"{fahrenheit}° in Fahrenheit is equivalent to {(fahrenheit-32)*5/9}° Celsius.")

  if unit == "C" or unit == "c":
    celsius = float(temp)
    print(f"{celsius}° in Celsius is equivalent to {celsius * 1.8 + 32}° Fahrenheit.")