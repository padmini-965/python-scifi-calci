from tkinter import *
import math
def click(value):
    last=entryfield.get()
    ans=''
    try:

        if value=='C':
            
            last=last[0:len(last)-1]
            entryfield.delete(0,END)
            entryfield.insert(0,last)

        elif value=='CE':
            entryfield.delete(0,END)

        elif value=='Sq':
            ans=math.sqrt(eval(last))
        
        
        elif value=='pi':
            ans=math.pi
        
        elif value=='cos':
            ans=math.cos(math.radians(eval(last)))

        elif value=='sin':
            ans=math.sin(math.radians(eval(last)))

        elif value=='tan':
            ans=math.tan(math.radians(eval(last)))

        elif value=='2pi':
            ans=2*math.pi

        elif value=='cosh':
            ans=math.cosh(math.radians(eval(last)))

        elif value=='sinh':
            ans=math.sinh(math.radians(eval(last)))

        elif value=='tanh':
            ans=math.tanh(math.radians(eval(last)))

        elif value==chr(8731):
            ans=eval(last)**(1/3)

        elif value=='x\u02b8':
            entryfield.insert(END,'**')
            return

        elif value=='x\u00B3':
            ans=eval(last)**3

        elif value=='x\u00B2':
            ans=eval(last)**2
        
        elif value=='ln':
            ans=math.log2(eval(last))
        
        elif value=='deg':
            ans=math.degrees(eval(last))
        
        elif value=='rad':
            ans=math.radians(eval(last))

        elif value=='e':
            ans=math.e

        elif value=='log10':
            ans=math.log10(eval(last))
        
        elif value=='x!':
            ans=math.factorial(eval(last))
        
        elif value==chr(247):
            entryfield.insert(END,"/")
            return 
        
        elif value=='=':
            ans=eval(last)
        
        else:
            entryfield.insert(END,value)
            return
    
    except SyntaxError:
        pass



    entryfield.delete(0,END)
    entryfield.insert(0,ans)

root=Tk()
root.title("CALCULATOR")
root.config(bg='lightblue')
root.geometry('680x486+300+100')
entryfield=Entry(root,font=('timesnewroman',25,'bold'),bg='white',fg='black',relief=SUNKEN,bd=10,width=40)
entryfield.grid(row=0,column=0,columnspan=8)
Button_text_list =["C","CE","Sq","+","pi","cos","sin","tan",
                   "1","2","3","-","2pi","cosh","tanh","sinh",
                   "4","5","6","*",chr(8731),"x\u00B3","x\u02b8","x\u00B2",
                   "7","8","9","/",chr(247),"ln","deg","rad","e",
                   "0","%","=","log10","(",")","x!"
                   ]


rowvalue=1
columnvalue=0

for i in Button_text_list:
    b1=Button(root,width=7,height=2,bd=2,relief=SUNKEN,text=i,bg='lightblue',fg='white',font=('arial,18,bold'),activebackground='white',command=lambda button=i: click(button))
    b1.grid(row=rowvalue,column=columnvalue,pady=1)
    columnvalue +=1
    if columnvalue>7:
        rowvalue+=1
        columnvalue=0





root.mainloop()