# Fahrenheit to Celcius
# F = Fahrenheit , C = Celcius

number = float(input("Enter the value: "))
select = int(input("For F to C: 1 , For C to F: 2 "))

if select == 1:
    result = (number - 32) / 1.8
    print(result)
elif select == 2:
    result = (number * 1.8) + 32
    print(result)
else:
    print("Incorrect Operation")         
