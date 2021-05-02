from tkinter import *
values= ""
def numberhandler(num, equations=None):
    global values
    values =values+str(num)
    equations.set(values)

win=Tk()
win.geometry('350x400')
win.config(bg="red")
ent_display=Entry(win,bg='black',bd=10,font=('arial',20,'bold'))
ent_display.grid(row=0,columnspan=4,pady=10)
#adding button in row first
btn9=Button(win,text='9',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler(9))
btn9.grid(row=1,column=0,pady=10)
btn8=Button(win,text='8',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler(8))
btn8.grid(row=1,column=1,pady=10)
btn7=Button(win,text='7',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler(7))
btn7.grid(row=1,column=2,pady=10)
btn6=Button(win,text='6',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler(6))
btn6.grid(row=1,column=3,pady=10)
#adding button  in 2nd row
btn5=Button(win,text='5',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler(5))
btn5.grid(row=2,column=0,pady=10)
btn4=Button(win,text='4',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler(4))
btn4.grid(row=2,column=1,pady=10)
btn3=Button(win,text='3',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler(3))
btn3.grid(row=2,column=2,pady=10)
btn2=Button(win,text='2',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler(2))
btn2.grid(row=2,column=3,pady=10)
#adding butto n in 3rd row
btn1=Button(win,text='1',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler(1))
btn1.grid(row=3,column=0,pady=10)
btn0=Button(win,text='0',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler(0))
btn0.grid(row=3,column=1,pady=10)
btn90=Button(win,text='+',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler('+'))
btn90.grid(row=3,column=2,pady=10)
btn91=Button(win,text='-',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler('-'))
btn91.grid(row=3,column=3,pady=10)
btn92=Button(win,text='*',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler('*'))
btn92.grid(row=4,column=0,pady=10)
btn93=Button(win,text='/',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler('/'))
btn93.grid(row=4,column=1,pady=10)
btn94=Button(win,text='C',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler('C'))
btn94.grid(row=4,column=2,pady=10)
btn95=Button(win,text='C',bd=5 ,font=('arial',20,'bold'),bg='yellow',command=lambda:numberhandler('='))
btn95.grid(row=4,column=3,pady=10)






win.mainloop()