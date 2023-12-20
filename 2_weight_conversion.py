# python weight converter

weight=float(input("enter weight: "))
unit=input("kilogram or gram ? (k or g): ")
if unit == 'k':
    weight=weight*1000
    unit="gram"
elif unit=='g':
    weight=weight/1000
    unit="kg"
else:
    print(f"{unit} is invalid")
print(f"your weight is {weight} {unit}")