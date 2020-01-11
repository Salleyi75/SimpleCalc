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

testvalues = [
    [2.0,5.0,"+",7],
    [2.78,6.78,"+",9.56],
    [5.0,6.0,"*",30.0],
    [5.0,6.0,"**",15625.0],
    [10.0,25.0,"/",0.4],
    [10.0,25.0,"*",250.0],
    [10.0,25.0,"-",-15.0]
]

for i in testvalues:
    if calc.operate(i[0],i[1],i[2]) == i[3]:
        print(str(i).ljust(50," "),"pass")
    else:
        print(str(i).ljust(50," "),"fail")

