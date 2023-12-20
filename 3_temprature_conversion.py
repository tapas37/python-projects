# python temprature conversion

unit=input("is the temprature in celcius or fahrenheit (c/f) : ")
temp=float(input("enter the temprature: "))
if unit == "c":
    temp=round((temp * (9/5))+32,2)
    unit="fahrenheit"
elif unit=="f":
    temp=round((temp-32)*5/9,2)
    unit="celcius"
else:
    print(f"{unit} is not valid")
print(f"the temprature is {temp} degree {unit}")