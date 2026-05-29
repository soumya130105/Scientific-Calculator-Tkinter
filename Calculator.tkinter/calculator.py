from tkinter import *
import math

first_number=second_number=operator=None

def get_digit(digit):
    current= result_label['text']
    new = current + str(digit)
    result_label.config(text=new)


def get_operator(op):
    global first_number,operator

    first_number=float(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_number,second_number,operator
    second_number = float(result_label['text'])
    if operator =='+':
        result_label.config(text=str(first_number+second_number))
    elif operator =='-':
        result_label.config(text=str(first_number-second_number))
    elif operator =='*':
        result_label.config(text=str(first_number*second_number))
    else:
        if second_number == 0:
                result_label.config(text='Error')
        else:
                result_label.config(text=str(round(first_number/second_number,3)))

def get_sqrt():
    if result_label['text'] =='':
         return
    number = float(result_label['text'])
    result_label.config(text=str(round(math.sqrt(number),3)))

def get_square():
    number = float(result_label['text'])
    result_label.config(text=str(number ** 2))

def get_dot():
    current = result_label['text']

    if '.' not in current:
        result_label.config(text=current + '.')

def get_percentage():
    number = float(result_label['text'])
    result_label.config(text=str(number/100))

def backspace():
    current = result_label['text']
    result_label.config(text=current[:-1])

def clear():
    result_label.config(text='')

root = Tk()

root.title('Calculator')
root.iconbitmap('calculator.ico')
root.geometry('280x442')
root.resizable(0,0)
root.configure(background='black')

result_label = Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=20,pady=(50,25),sticky='w')
result_label.configure(font=('verdana',30,'bold'))

btn_root=Button(root,text='√',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_sqrt())
btn_root.grid(row=1,column=0)
btn_root.config(font=('verdana',14))

btn_square=Button(root,text='x²',bg='#1e1e1e',fg='white',width=5,height=2,command=get_square)
btn_square.grid(row=1,column=1)
btn_square.config(font=('verdana',14))

btn_per=Button(root,text='%',bg='#1e1e1e',fg='white',width=5,height=2,command=get_percentage)
btn_per.grid(row=1,column=2)
btn_per.config(font=('verdana',14))

btn_del=Button(root,text='D',bg='#1e1e1e',fg='white',width=5,height=2,command=backspace)
btn_del.grid(row=1,column=3)
btn_del.config(font=('verdana',14))

btn_dot=Button(root,text='.',bg='#1e1e1e',fg='white',width=5,height=2,command=get_dot)
btn_dot.grid(row=5,column=0)
btn_dot.config(font=('verdana',14))

btn7=Button(root,text='7',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_digit(7))
btn7.grid(row=2,column=0)
btn7.config(font=('verdana',14))

btn8=Button(root,text='8',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=2,column=1)
btn8.config(font=('verdana',14))

btn9=Button(root,text='9',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_digit(9))
btn9.grid(row=2,column=2)
btn9.config(font=('verdana',14))

btn_add=Button(root,text='+',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_operator('+'))
btn_add.grid(row=2,column=3)
btn_add.config(font=('verdana',14))

btn4=Button(root,text='4',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=3,column=0)
btn4.config(font=('verdana',14))

btn5=Button(root,text='5',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=3,column=1)
btn5.config(font=('verdana',14))

btn6=Button(root,text='6',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=3,column=2)
btn6.config(font=('verdana',14))

btn_sub=Button(root,text='-',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_operator('-'))
btn_sub.grid(row=3,column=3)
btn_sub.config(font=('verdana',14))

btn1=Button(root,text='1',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=4,column=0)
btn1.config(font=('verdana',14))

btn2=Button(root,text='2',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=4,column=1)
btn2.config(font=('verdana',14))

btn3=Button(root,text='3',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=4,column=2)
btn3.config(font=('verdana',14))

btn_mul=Button(root,text='*',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_operator('*'))
btn_mul.grid(row=4,column=3)
btn_mul.config(font=('verdana',14))

btn0=Button(root,text='0',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_digit(0))
btn0.grid(row=5,column=1)
btn0.config(font=('verdana',14))

btn_equal=Button(root,text='=',bg='#1e1e1e',fg='white',width=5,height=2,command=get_result)
btn_equal.grid(row=5,column=2)
btn_equal.config(font=('verdana',14))

btn_div=Button(root,text='/',bg='#1e1e1e',fg='white',width=5,height=2,command=lambda:get_operator('/'))
btn_div.grid(row=5,column=3)
btn_div.config(font=('verdana',14))

btn_clr = Button(root,text='CLR',bg='#3b82f6',fg='white',font=('verdana',8,'bold'),bd=0,padx=3,pady=1,command=clear)
btn_clr.place(x=240, y=15)

root.mainloop()