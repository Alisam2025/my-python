int_num = int(input("Enter a number: "))
x = None 
#print positive or negative
while x != 0:
    if int_num > 0:
        print("Positive")
    elif int_num < 0:
        print("Negative")
    else:
        print("Zero")
    break
