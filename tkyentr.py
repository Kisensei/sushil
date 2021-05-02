from tkinter import *
from tkinter import messagebox
def eventhandler(e):
    messagebox.showinfo('your system is hacked','your system is hacked')
win=Tk()
win.title('app')
win.geometry('2000x1000')
win['background']=("blue")
btn_click=Button(win,text='click',bg='grey',fg='red',font=('Playfair Display',60,"italic"))
btn_click.grid(row=0,column=1,padx=10,pady=30)
btn_click.bind('<Button-1>',eventhandler)
btn_click2=Button(win,text='click',bg='orange',fg='red',font=('Playfair Display',80,"italic"))
btn_click2.grid(row=1,columnspan=2,padx=20,pady=56)
btn_click3=Button(win,text='click',bg='violet',fg='red',font=('Playfair Display',50,"italic"))
btn_click3.grid(row=1,column=3,padx=20,pady=56)
btn_click4=Button(win,text='click',bg='violet',fg='red',font=('calibri',30,"italic"))
btn_click4.place(x=100,y=200)
win.mainloop()