"""This is a calculator program that helps you do simple mathematical operations"""

print("calculator started".center(40,"*"))

class calc:
    """Contains all operations needed for the calculator"""

    last_value:float
    ops = {
            "+": lambda x,y : x + y ,
            "-": lambda x,y : x - y ,
            "*": lambda x,y : x * y ,
            "/": lambda x,y : x / y ,
            "**": lambda x,y : x ** y
        }

    
    @staticmethod
    def operate (num1:float, num2:float, operation:str) -> float:
        last_value = calc.ops[operation](num1,num2)
        return last_value

