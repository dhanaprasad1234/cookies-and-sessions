cal=int(input("Enter the opertion 1.add 2.sub 3.mul 4.div : "))
cal1=str(cal)
num1=int(input("Enter The First Number"))
num2=int(input("Enter The Second Numbe"))

for choice in cal1:
    if choice == '1':
        print("The Sum Of Numbers",num1+num2)
        break
    elif choice == '2':
        print("The Sub Of Numbers ",num1-num2)
        break
    elif choice == '3':
        print("The Mul Of Numbers",num1*num2)
        break
    elif choice == '4':
        print("The Div Of Numbers",num1/num2)
        break
else:
    print("Invalid Input")
