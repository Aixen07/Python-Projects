# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
while True:
    try:
        num_1 = float(input("\nEnter 1st Number: "))
        num_2 = float(input("Enter 2nd Number: "))
        
        print("\nWhat Operation you want to perform?\n+ For addition\n- For Substraction\n* For Multiplication\n/ For Division")
        
        a = input("\nEnter Operation: ")
        
        match a:
            case "+":
                print(f"The Addition is {num_1+num_2}")
            case "-": 
                print(f"The Subtraction is {num_1-num_2}")
            case "*":
                print(f"The Multiplication is {num_1*num_2}")
            case "/":
                if num_2==0:
                    print("Hey, Don't Divide by Zero")
                else: 
                    print(f"The Division is {num_1/num_2}")
            case _:
                print("Invalid Operator!")
        choice = input("\nPress q to exit: ")
        if choice.lower()=="q":
            break
        
    except ValueError:
        print("\nPlease enter valid numbers only!")

        
        
        