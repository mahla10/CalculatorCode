Def calculator():
    Print(“Welcome to Simple Calculator!”)
    While True:
        Try:
            Num1 = float(input(“Enter the first number: “))
            Operator = input(“Enter the operator (+, -, *, /): “)
            Num2 = float(input(“Enter the second number: “))
            
            If operator == ‘+’:
                Result = num1 + num2
            Elif operator == ‘-‘:
                Result = num1 – num2
            Elif operator == ‘*’:
                Result = num1 * num2
            Elif operator == ‘/’:
                If num2 == 0:
                    Print(“Error: Division by zero!”)
                    Continue
                Else:
                    Result = num1 / num2
            Else:
                Print(“Invalid operator!”)
                Continue
            
            Print(“Result:”, result)
            
            Choice = input(“Do you want to perform another calculation? (yes/no): “)
            If choice.lower() != ‘yes’:
                Break
        
        Except ValueError:
            Print(“Error: Please enter valid numbers!”)
        Except Exception as e:
            Print(“An error occurred:”, e)

Calculator()
