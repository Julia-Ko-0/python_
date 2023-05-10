from tkinter import*
from math import*

tk = Tk()
tk.title('график функции')
tk.geometry('500x500')

def createLine(*event):
    # selection = btnFunct.get()
    

    canv.create_line(50,0,50,500)
    canv.create_line(0,400,500,400)
    x0 = 50
    y0 = 400
    y= 10
    x = 10
    for i in range(100):
        canv.create_line(45,y,55,y)
        canv.create_line(x,395,x,405)
        y += 20
        x += 20
   
    x1 = 50
    y1 =400
    # if selection=='0 y=a*x+b':

    #     for i in range(1000):
    #         canv.create_line(x1,y1,x1+1,y1+1,fill='blue')
    #         x1+=1
    #         y1-=1
    # elif selection == '1 y=a+b/x':
    #        for i in range(1000):
    #         canv.create_line(x1,y1,x1+1,y1+1,fill='blue')
    #         x1+=1
    #         y1+=1   
    # for i in range(1000):
    #     canv.create_line(x1,y1,x1+1,y1+1,fill='blue')
    #     x1+=1
    #     y1=(1+x1*1)  
    canv.create_line(x0,y0,x0+500,y0-500,fill='blue')
    # if f =='0':
    #     canv.delete('all')

      
    
    
 
OptionList = ['0 y=a*x+b','1 y=a+b/x','2 y=a*x^b'] 


startText =StringVar(tk)
startText.set('0 y=a*x+b')
text = Label(text='выбор: ').place(x=0,y=0)
btnExint = Button(text='закрыть',command=tk.quit).place(x=440, y=0,width=60, height=30)
btnFunct = OptionMenu(tk,startText,*OptionList ).place(x=42, y=0,width=100, height=30)


canv = Canvas(tk,width=500,height=470,bg='#BEC9D5',borderwidth=2)
canv.place(y=30)
createLine()

tk.mainloop()
