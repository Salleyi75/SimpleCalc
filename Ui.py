import tkinter

def Equalize_Grid(grid_owner):
    """This function gives equal weight to each and every existing row and column in a tkinter grid
        Grid_Owner -- parent object that owns the grid"""
    weighter = {0: lambda x, y: x.columnconfigure(y,weight=1) , 1: lambda x,y: x.rowconfigure(y,weight=1)}

    count = 0
    for y in grid_owner.grid_size():
        for i in range(0,y):
            weighter[count](grid_owner,i)
        count += 1




#### CODING BEGINS ####
root = tkinter.Tk(className="Calculator")
root.title("Calculator")
root.geometry("300x450")
root.resizable(False,False)

##main container

##main_style.configure("My.MFrame", background='red')

mainframe = tkinter.Frame(root,bg="red")
mainframe.pack(fill=tkinter.BOTH, expand = 1)

output_scr = tkinter.Label(mainframe,text ="0.00",anchor=tkinter.SE,font="TIMES 20")
output_scr.grid(column=0,row=0,columnspan=4,sticky="nsew")

##CREATE BUTTONS LOOP
num_but = []
op_but  = []


##Creating Button 1 to 9
for i in range(1,10):
    curbut = tkinter.Button(mainframe, text=str(i))

    curbut.grid(row= 3 - ((i-1)//3), column = (i-1)%3 )
    num_but.append(curbut)  

##Creating Buttons + , - , / , *
for i in {"+":1,"-":2,"/":3,"*":4}.items():
    curbut = tkinter.Button(mainframe, text = i[0])
    curbut.grid(row=i[1],column=3)
    op_but.append(curbut)

##Creating Button 0
curbut = tkinter.Button(mainframe, text="0")
curbut.grid(row=4,column=0,columnspan=2)
num_but.append(curbut)

##Creating Button .
curbut = tkinter.Button(mainframe, text= ".")
curbut.grid(row=4,column=2)
num_but.append(curbut)

##Creating Button =
curbut = tkinter.Button(mainframe, text="=")
curbut.grid(row=5,column=0,columnspan=4)
op_but.append(curbut)

num_but = tuple(num_but)
op_but = tuple(op_but)

##Expand each button to fill its grid cell
for i in num_but + op_but:
    i.grid(sticky = "nswe")


Equalize_Grid(mainframe)

print("\n\n")

##START WINDOW
root.mainloop()
