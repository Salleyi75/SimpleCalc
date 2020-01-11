import tkinter

root = tkinter.Tk(className="Calculator")
root.geometry("300x450")
root.resizable(False,False)

##main container

##main_style.configure("My.MFrame", background='red')

mainframe = tkinter.Frame(root,bg="red")
mainframe.pack(fill=tkinter.BOTH, expand = 1)

output_scr = tkinter.Label(mainframe,text ="Hello World")
output_scr.grid(column=0,row=0,columnspan=4,sticky="nsew")

##CREATE BUTTONS LOOP
listbut = []

##Creating Button 1 to 9
for i in range(1,10):
    curbut = tkinter.Button(mainframe, text=str(i))

    curbut.grid(row= 3 - ((i-1)//3), column = (i-1)%3 )
    listbut.append(curbut)  

##Creating Buttons + , - , / , *
for i in {"+":1,"-":2,"/":3,"*":4}.items():
    curbut = tkinter.Button(mainframe, text = i[0])
    curbut.grid(row=i[1],column=3)
    listbut.append(curbut)

##Creating Button 0
curbut = tkinter.Button(mainframe, text="0")
curbut.grid(row=4,column=0,columnspan=2, sticky="nswe")

##Creating Button .
curbut = tkinter.Button(mainframe, text= ".")
curbut.grid(row=4,column=2)

##Creating Button =
curbut = tkinter.Button(mainframe, text="=")
curbut.grid(row=5,column=0,columnspan=4,sticky="nswe")

##START WINDOW
root.mainloop()
